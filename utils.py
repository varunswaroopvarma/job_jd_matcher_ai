from PyPDF2 import PdfReader

def extract_text_from_file(uploaded_file):
    """
    Extract text from PDF or TXT resume file.
    """
    filename = uploaded_file.filename.lower()

    if filename.endswith(".pdf"):
        reader = PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text.strip()

    elif filename.endswith(".txt"):
        return uploaded_file.read().decode("utf-8", errors="ignore").strip()

    else:
        return "Unsupported file format. Please upload PDF or TXT."
