import spacy

nlp = spacy.load("pt_core_news_sm")

def interpretar_regras(texto):
    doc = nlp(texto)
    entidades = [(ent.text, ent.label_) for ent in doc.ents]
    return entidades

if __name__ == "__main__":
    import json

    with open("../output/regras_extraidas.json", "r", encoding="utf-8") as f:
        dados = json.load(f)

    for reg, textos in dados.items():
        print(f"\n📌 Interpretando Registro {reg}:")
        for texto in textos:
            entidades = interpretar_regras(texto)
            print(f"➡ {texto[:100]}...")
            print(f"🔍 Entidades: {entidades}")
