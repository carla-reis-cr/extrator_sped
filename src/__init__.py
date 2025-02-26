# src/__init__.py

# Reexportar funções principais para facilitar imports
from .pdf_parser import extract_text_from_pdf
from .nlp_processor import load_nlp_model, extract_rules
from .data_handler import create_dataframe, export_to_csv
#from .db_integration import connect_to_db, insert_data
from .utils import clean_text

# Definir o que é exportado com `from src import *`
__all__ = [
    "extract_text_from_pdf",
    "load_nlp_model",
    "extract_rules",
    "create_dataframe",
    "export_to_csv",
   # "connect_to_db",
   # "insert_data",
    "clean_text"
]

# Código de inicialização (opcional)
print("Módulo src carregado com sucesso!")