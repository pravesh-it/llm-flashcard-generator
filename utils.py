import PyPDF2

def read_pdf(file):
    reader = PyPDF2.PdfReader(file)
    return "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])

def read_txt(file):
    return file.read().decode("utf-8")
