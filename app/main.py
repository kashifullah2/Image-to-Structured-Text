from fastapi import FastAPI, UploadFile, Request, Form, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from services.extractor import Extractor
from services.text_fixer import TextFixer
import json

app = FastAPI()

# Static and templates
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/add", response_class=HTMLResponse)
async def upload_files(
    request: Request,
    files: list[UploadFile] = File(...),
    fields: str = Form(...)
):
    results = []

    for file in files:
        extractor = Extractor(file)
        image_to_text = await extractor.extract_text()

        fix_text = TextFixer(image_to_text, fields=fields).text_fixer()
        final = fix_text.strip().removeprefix("```json").removesuffix("```").strip()
        data = json.loads(final)
        results.append(data)

    # Render results.html
    return templates.TemplateResponse(
        "result.html", {"request": request, "results": results}
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)
