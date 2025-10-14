from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

class TextFixer:
    def __init__(self,text,fields:str = "extract features which is important"):
        self.text = text
        self.fields = fields
        self.model = ChatGoogleGenerativeAI(model="gemini-2.0-flash",api_key=api_key)
    
    def text_fixer(self):
        # field_list = "\n".join([f"- {f}" for f in self.fields])
        prompt = f"""
        Extract the following fields from the given text:
        {self.fields}

        Text:
        {self.text}

        Return result in JSON format. also fix the spellings.
        """
        return self.model.invoke(prompt).content    