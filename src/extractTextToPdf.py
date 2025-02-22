
import fitz

def extract_text_from_pdf(pdf_path):
    """Extrai todo o texto do PDF."""
    doc = fitz.open(pdf_path)
    txtExtractToPdf = "\n".join([page.get_text("text") for page in doc])
    
    return txtExtractToPdf


