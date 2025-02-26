import spacy
from spacy.pipeline import EntityRuler
import re

def load_nlp_model():
    # Carrega o modelo spaCy para português
    nlp = spacy.load("pt_core_news_sm")

    # Adiciona regras personalizadas para reconhecer termos do SPED Fiscal
    ruler = EntityRuler(nlp)
    
    # Lista de padrões baseados no manual do SPED Fiscal
    patterns = [
        # Registros
        {"label": "REG", "pattern": "C100"},
        {"label": "REG", "pattern": "C170"},
        {"label": "REG", "pattern": "C190"},
        {"label": "REG", "pattern": "C500"},

        # Campos
        {"label": "FIELD", "pattern": "CFOP"},
        {"label": "FIELD", "pattern": "CST"},
        {"label": "FIELD", "pattern": "NCM"},

        # Validações (ex: "deve ser preenchido")
        {"label": "VALIDATION", "pattern": [{"LOWER": "deve"}, {"LOWER": "ser"}, {"LOWER": "preenchido"}]},
        {"label": "VALIDATION", "pattern": [{"LOWER": "deve"}, {"LOWER": "conter"}]},
        {"label": "VALIDATION", "pattern": [{"LOWER": "obrigatório"}]},

        # Tabelas (ex: "Tabela 1.1")
        {"label": "TABLE", "pattern": [{"LOWER": "tabela"}, {"SHAPE": "d.d"}]},
        {"label": "TABLE", "pattern": [{"LOWER": "tabela"}, {"SHAPE": "d.d.d"}]},
    ]
    
    # Adiciona os padrões ao EntityRuler
    ruler.add_patterns(patterns)
    
    # Adiciona o EntityRuler ao pipeline do spaCy
    nlp.add_pipe("entity_ruler", name="sped_ruler").add_patterns(patterns)
    
    return nlp

def extract_rules(text, nlp_model):
    # Processa o texto com o modelo spaCy
    doc = nlp_model(text)
    rules = []
    
    # Extrair entidades nomeadas
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
       # Extrair regras específicas
    for sent in doc.sents:
        # Verifica se a sentença contém uma validação
        if any(ent.label_ == "VALIDATION" for ent in sent.ents):
            # Extrai o registro, campo e tabela associados
            registro = next((ent.text for ent in sent.ents if ent.label_ == "REG"), None)
            campo = next((ent.text for ent in sent.ents if ent.label_ == "FIELD"), None)
            tabela = next((ent.text for ent in sent.ents if ent.label_ == "TABLE"), None)
            
            if registro or campo or tabela:
                rules.append({
                    "Registro": registro,
                    "Campo": campo,
                    "Validação": sent.text,
                    "Tabela": tabela
                })
    
    return rules, entities

def save_entities_to_txt(entities, file_path):
    # Salva as entidades em um arquivo TXT
    with open(file_path, "w", encoding="utf-8") as file:
        for entity, label in entities:
            file.write(f"Entidade: {entity} | Tipo: {label}\n")