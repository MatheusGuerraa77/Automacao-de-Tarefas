import PyPDF2 as pdf
from PyPDF2 import PdfReader

def get_pdf_metadata(pdf_path):
    with open(pdf_path, 'rb') as f:
        reader = PdfReader(f)
        info = reader.metadata
    return info

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as f:
        reader = PdfReader(f)
        results = []
        for i in range(0,len(reader.pages)):
            selected_page = reader.pages[i]
            text = selected_page.extract_text()
            results.append(text)
        return ' '.join(results)

#Buscando dados e Metadados de um arquivo pdf
print(get_pdf_metadata('files/sample.pdf'))
print(extract_text_from_pdf('files/sample.pdf'))