# 📸 Smart Image Text Extractor

It users upload one or multiple invoice or receipt images, specify the fields they want to extract (e.g., amount, total amount, sent by, company name, date), and uses OCR (Tesseract or EasyOCR) to extract those fields automatically. The extracted information is returned in structured JSON format,
## ⚡ Features

- Upload **single or multiple images**  
- Preview images in a **carousel**  
- Extract text using **OCR**  
- Structure text in **JSON** via Gemini/LLM  
- Save structured data to **CSV**

---

### Applications

- Extract data from receipts, invoices, bank slips, or payment screenshots.  
- Automate business reporting and record keeping.  
- Convert handwritten or printed forms into structured CSV/JSON.  
- Extract text from study materials or scanned notes.  

---

## 🛠 Installation


### 1. Clone the repository

```bash
git clone https://github.com/yourusername/image-text-extractor.git
cd image-text-extractor


First get the Google Gemini API paste it .env file

pip install -r requirements.txt


run main.py file


use uv python package manager for virtual env

uv run main.py file
