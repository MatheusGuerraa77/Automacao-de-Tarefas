import PyPDF2 as pdf
from PyPDF2 import PdfReader, PdfWriter
import  os
from PIL import Image

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


def split_pdf(pdf_path):
    with open(pdf_path, 'rb') as f:
        reader = PdfReader(f)
        for page_num in range(0, len(reader.pages)):
            selected_page = reader.pages[page_num]
            writer = PdfWriter()
            writer.add_page(selected_page)
            # print(os.path.split(pdf_path)[1])
            filename = os.path.split(pdf_path)[1]
            new_filename = f'files/{filename}_{page_num+1}.pdf'
            with open(new_filename, 'wb') as out:
                writer.write(out)
            print(f'PDF criado com o nome: {new_filename}')


def convert_img_pdf(image_file):
    my_image = Image.open(image_file)
    # print(my_image)
    img = my_image.convert('RGB')
    # print(os.path.splitext(image_file)[0])
    filename = f'{os.path.splitext(image_file)[0]}.pdf'
    img.save(filename)






# 1 - Buscando dados e Metadados de um arquivo pdf
# print(get_pdf_metadata('files/sample.pdf'))
# print(extract_text_from_pdf('files/sample.pdf'))

# 2 - Dividindo PDF por página
# split_pdf('files/sample.pdf')

# 7 - Converte imagem em pdf
convert_img_pdf('files/img.png')