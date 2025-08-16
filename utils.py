from PyPDF2 import PdfReader

def extract_text_from_pdf(file):
    """Extract text from a PDF file"""
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text.strip()

def extract_text_from_txt(file):
    """Extract text from a TXT file"""
    return file.read().decode("utf-8").strip()
