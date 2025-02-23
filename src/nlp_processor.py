import spacy
import re

def load_nlp_model():
    return spacy.load("pt_core_news_sm")

def extract_rules(text, nlp_model):
    doc = nlp_model(text)
    rules = []
    for sent in doc.sents:
        if "deve ser preenchido" in sent.text:
            match = re.search(r"O campo (\w+) deve ser preenchido com valores da tabela (\d+\.\d+)", sent.text)
            if match:
                rules.append({
                    "Registro": match.group(1),
                    "Campo": match.group(1),
                    "Validação": f"Preenchimento com valores da tabela {match.group(2)}",
                    "Versão": "1.0",
                    "Dependência": f"Tabela {match.group(2)}",
                    "Tabela": match.group(2)
                })
    return rules