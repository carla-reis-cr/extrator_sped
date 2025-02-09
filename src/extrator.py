import fitz  # PyMuPDF
import re
import json
import os

def extrair_texto_pdf(caminho_pdf):
    """Extrai todo o texto do Guia Prático da EFD ICMS/IPI."""
    doc = fitz.open(caminho_pdf)
    texto_completo = "\n".join([pagina.get_text("text") for pagina in doc])
    return texto_completo

def extrair_regras(texto, registros=["0200", "0205"]):
    """Identifica e separa as regras dos registros especificados."""
    regras = {}

    for registro in registros:
        padrao = rf"(REGISTRO {registro}.*?)\n\n"
        correspondencias = re.findall(padrao, texto, re.DOTALL)

        if correspondencias:
            regras[registro] = correspondencias[0]  # Salvar o bloco do registro

    return regras

def salvar_regras(regras, caminho_saida="output/regras_extraidas.json"):
    """Salva as regras extraídas em um arquivo JSON."""
    os.makedirs(os.path.dirname(caminho_saida), exist_ok=True)
    
    with open(caminho_saida, "w", encoding="utf-8") as f:
        json.dump(regras, f, ensure_ascii=False, indent=4)

    print(f"Regras extraídas e salvas em {caminho_saida}")

if __name__ == "__main__":
    caminho_pdf = "data/guia_pratico_efd_icms_ipi.pdf"  # Ajuste o caminho conforme necessário

    if not os.path.exists(caminho_pdf):
        print(f"Erro: Arquivo não encontrado em {caminho_pdf}")
    else:
        texto = extrair_texto_pdf(caminho_pdf)
        regras_extraidas = extrair_regras(texto)
        salvar_regras(regras_extraidas)
