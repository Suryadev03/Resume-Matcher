from pypdf import PdfReader

def extract_text(file_path):
    pdf = PdfReader(file_path)
    text = ""
    for page in pdf.pages:
        content = page.extract_text()
        text += content + "\n"

    return text
