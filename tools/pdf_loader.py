from pypdf import PdfReader

def load_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        text += page.extract_text() + "\n"
    
    return text

def load_pdf_with_pages(file_path):
    reader = PdfReader(file_path)
    documents = []

    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        documents.append({"page": i+1, "text": text})
    
    return documents
