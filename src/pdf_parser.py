import PyPDF2
from src.utils import clean_text

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()

        text = clean_text(text)
        with open("data/output/text_extract.txt", "w") as arquivo:
            arquivo.write(text)
        #return text