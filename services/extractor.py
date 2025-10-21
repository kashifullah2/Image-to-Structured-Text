# from PIL import Image
# import pytesseract
# import easyocr

# class Extractor:
#     def __init__(self,image_path,method="pytesseract"):
#         self.image_path = image_path
#         self.method = method

#     def extract_text(self):
#         if self.method=="pytesseract":
#             img = Image.open(self.image_path)
#             text = pytesseract.image_to_string(img)
#             return text
#         else:
#             reader = easyocr.Reader(['en'])
#             results = reader.readtext(self.image_path)
#             return " ".join([text for (_, text, _) in results])


from PIL import Image
import pytesseract
import easyocr
import tempfile

class Extractor:
    def __init__(self, upload_file, method="pytesseract"):
        self.upload_file = upload_file
        self.method = method

    async def extract_text(self):
        # Save uploaded file temporarily
        contents = await self.upload_file.read()
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
            tmp.write(contents)
            tmp_path = tmp.name

        # Use pytesseract or easyocr
        if self.method == "pytesseract":
            img = Image.open(tmp_path)
            text = pytesseract.image_to_string(img)
        else:
            reader = easyocr.Reader(['en'])
            results = reader.readtext(tmp_path)
            text = " ".join([txt for (_, txt, _) in results])

        return text
    