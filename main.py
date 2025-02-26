from src.pdf_parser import extract_text_from_pdf
from src.utils import clean_text
from src.data_handler import create_dataframe, export_to_csv
from src.nlp_processor import load_nlp_model, extract_rules, save_entities_to_txt

def main():
    # Caminhos dos arquivos
    pdf_path = "data/input/efd_icms_ipi_3.1.7.pdf"
    csv_output_path = "data/output/regras_sped.csv"
    # 1. Extrair texto do PDF
    print("Extraindo texto do PDF...")
    text = extract_text_from_pdf(pdf_path)
    text = clean_text(text)

    # 2. Processar texto com NLP
    print("Processando texto com NLP...")
    nlp_model = load_nlp_model()
    nlp_model.max_length = 5000000
    rules, entities = extract_rules(text, nlp_model)

    save_entities_to_txt(entities, "data/output/entidades.txt")

    # 3. Criar DataFrame e exportar para CSV
    print("Exportando regras para CSV...")
    df = create_dataframe(rules)
    export_to_csv(df, csv_output_path)

    # 4. Integrar com banco de dados
    #print("Inserindo dados no banco de dados...")
    #engine = connect_to_db(db_connection_string)
    #insert_data(df, table_name, engine)

    print("Processo concluído!")

if __name__ == "__main__":
    main()