# import json
# from fastapi import APIRouter, Request, UploadFile, Form
# from fastapi.responses import HTMLResponse
# from app.services.extractor import Extractor
# from app.services.text_fixer import TextFixer
# from app.utils.csv_utils import save_to_csv

# router = APIRouter()

# @router.post("/upload", response_class=HTMLResponse)
# async def upload_image(request: Request, file: UploadFile):
#     # Step 1: Extract text
#     text = Extractor(file.file).extract_text()

#     # Step 2: Fix text
#     fixer = TextFixer(text,fields)
#     structured = fixer.text_fixer()

#     # Step 3: Clean and parse JSON output
#     structured = structured.strip().removeprefix("```json").removesuffix("```").strip()

#     try:
#         structured_json = json.loads(structured)
#     except json.JSONDecodeError:
#         return HTMLResponse("<h3>❌ Invalid JSON output from model</h3>", status_code=400)

#     # Step 4: Save to CSV
#     save_to_csv(structured_json)

#     return HTMLResponse("<h3>✅ Extraction complete! Data saved to output.csv</h3>")
