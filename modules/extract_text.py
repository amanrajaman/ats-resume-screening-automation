import PyPDF2
import docx
import re
import os

def extract_text(file_path):
    """
    Extract text from PDF or DOCX file based on extension
    """
    ext = os.path.splitext(file_path)[1].lower()
    
    if ext == ".pdf":
        return extract_text_from_pdf(file_path)
    elif ext == ".docx":
        return extract_text_from_docx(file_path)
    else:
        print(f"Unsupported file format: {file_path}")
        return ""

def extract_text_from_pdf(file_path):
    text = ""
    try:
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + " "
    except Exception as e:
        print(f"Error reading PDF {file_path}: {e}")
    return clean_text(text)

def extract_text_from_docx(file_path):
    text = ""
    try:
        doc = docx.Document(file_path)
        for para in doc.paragraphs:
            text += para.text + " "
    except Exception as e:
        print(f"Error reading DOCX {file_path}: {e}")
    return clean_text(text)

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces/newlines with single space
    text = re.sub(r'[^a-z0-9\s]', '', text)  # Keep only alphanumeric & space
    return text.strip()


if __name__ == "__main__":
    test_files = [
        "data/resumes/Aman Raj Aman.pdf",
        "data/resumes/Aman Raj Aman.docx"
    ]
    
    for file in test_files:
        print(f"Extracting: {file}")
        extracted = extract_text(file)
        print(extracted[:1000])  # Preview first 500 characters
        print("-" * 50)
