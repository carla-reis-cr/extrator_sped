import re

def extrair_registros(texto):
    padrao_0200 = r"REGISTRO 0200(.*?)(?=REGISTRO 0205|REGISTRO \d+|$)"
    padrao_0205 = r"REGISTRO 0205(.*?)(?=REGISTRO \d+|$)"

    registro_0200 = re.findall(padrao_0200, texto, re.DOTALL)
    registro_0205 = re.findall(padrao_0205, texto, re.DOTALL)

    return {
        "0200": registro_0200,
        "0205": registro_0205
    }

if __name__ == "__main__":
    with open("../output/texto_extraido.txt", "r", encoding="utf-8") as f:
        texto = f.read()

    registros = extrair_registros(texto)

    with open("../output/regras_extraidas.json", "w", encoding="utf-8") as f:
        import json
        json.dump(registros, f, ensure_ascii=False, indent=4)

    print("Regras extraídas e salvas!")
