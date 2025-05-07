import PyPDF2
import os
from langdetect import detect


def read_txt_file(filepath: str) -> str:
    """Read content from a .txt file."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        return content
    except Exception as e:
        print(f"❌ Error reading TXT file: {e}")
        return ""


def read_pdf_file(filepath: str) -> str:
    """Extract text from a PDF file using PyPDF2."""
    try:
        with open(filepath, "rb") as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()
        return text.strip()
    except Exception as e:
        print(f"❌ Error reading PDF file: {e}")
        return ""


def read_file(filepath: str) -> str:
    """Read a file (txt or pdf) and return its content as text."""
    if os.path.splitext(filepath)[1].lower() == ".txt":
        return read_txt_file(filepath)
    elif os.path.splitext(filepath)[1].lower() == ".pdf":
        return read_pdf_file(filepath)
    else:
        print(f"❌ Unsupported file type: {filepath}")
        return ""


def detect_language(text: str) -> str:
    """Detect the language of the given text using langdetect."""
    try:
        return detect(text)
    except Exception:
        return "unknown"
