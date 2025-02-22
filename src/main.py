
from extractTextToPdf import extract_text_from_pdf 

if __name__ == "__main__":
    pdf_path = "data/guia_pratico_efd_icms_ipi.pdf"
    regras_extraidas = extract_text_from_pdf(pdf_path)

    print("Regras Extraídas:"+regras_extraidas)
   