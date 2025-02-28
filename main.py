import json
import os
from src.pdf_parser import extract_text_from_pdf
from src.utils import clean_text, read_arquive
from src.data_handler import create_dataframe, export_to_csv
from src.nlp_processor import load_nlp_model, extract_rules, save_entities_to_txt


STATUS_FILE = "status.json"

RULES = ''
# Caminhos dos arquivos
pdf_path = "data/input/efd_icms_ipi_3.1.7.pdf"
csv_output_path = "data/output/regras_sped.csv"

# Inicializa o status das etapas, se não existir
def load_status():
    if os.path.exists(STATUS_FILE):
        with open(STATUS_FILE, "r") as file:
            return json.load(file)
    return {"carregamento": False, "extração": False, "nlp": False, "exportação": False}

# Salva o status atualizado
def save_status(status):
    with open(STATUS_FILE, "w") as file:
        json.dump(status, file, indent=4)

# Simulação das funções para cada etapa
def carregar_modulo():
    print("✅ Módulo src carregado com sucesso!")
    
def extrair_texto():

    print("🔍 Extraindo texto do PDF...")


    # 1. Extrair texto do PDF
    print("Extraindo texto do PDF...")
    extract_text_from_pdf(pdf_path)
    
    print("✅ Texto extraído!")

def processar_nlp():
    print("🤖 Processando texto com NLP...")
    
     # 2. Processar texto com NLP
    print("Processando texto com NLP...")
    textNlp = read_arquive("data/output/text_extract.txt")
    nlp_model = load_nlp_model()
    nlp_model.max_length = 5000000
    RULES, entities = extract_rules(textNlp, nlp_model)

    save_entities_to_txt(entities, "data/output/entidades.txt")

    print("✅ Processamento concluído!")

def exportar_csv():
    print("📂 Exportando regras para CSV...")
    
    # 3. Criar DataFrame e exportar para CSV
    print("Exportando regras para CSV...")
    df = create_dataframe(RULES)
    export_to_csv(df, csv_output_path)

    print("✅ Exportação concluída!")


def integration_database():
    
    # 4. Integrar com banco de dados
    #print("Inserindo dados no banco de dados...")
    #engine = connect_to_db(db_connection_string)
    #insert_data(df, table_name, engine)

    print("Processo concluído!")

# Menu interativo
def menu():
    status = load_status()
    
    opcoes = {
        "1": ("Carregar módulo", carregar_modulo, "carregamento"),
        "2": ("Extrair texto do PDF", extrair_texto, "extração"),
        "3": ("Processar texto com NLP", processar_nlp, "nlp"),
        "4": ("Exportar regras para CSV", exportar_csv, "exportação"),
        "5": ("Sair", None, None)
    }

    while True:
        print("\n📌 **Selecione uma etapa para executar:**")
        for key, (desc, _, stage) in opcoes.items():
            if key != "5":
                status_txt = "✅ Concluído" if status[stage] else "🔴 Pendente"
                print(f"[{key}] {desc} - {status_txt}")
        print("[5] Sair")

        escolha = input("\nDigite a opção desejada: ")
        
        if escolha == "5":
            print("👋 Saindo...")
            break
        elif escolha in opcoes:
            _, func, stage = opcoes[escolha]
            
            if status[stage]:  # Se a etapa já foi concluída, perguntar se quer refazer
                refazer = input("Esta etapa já foi concluída. Deseja refazer? (s/n): ").strip().lower()
                if refazer != "s":
                    print("⏭ Pulando etapa.")
                    continue
            
            func()
            status[stage] = True
            save_status(status)
        else:
            print("⚠️ Opção inválida!")
            
if __name__ == "__main__":
    menu()