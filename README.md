# Extração e Validação de Regras do SPED (EFD ICMS/IPI)

## Descrição do Projeto

Este projeto tem como objetivo **extrair regras do Guia Prático da EFD ICMS/IPI** e utilizar **Inteligência Artificial (IA)** para validar registros fiscais, identificando possíveis erros nos dados do cliente.

## Estrutura do Projeto

```plaintext
extrator_sped/
│── data/                  # Pasta para armazenar o PDFs dos testes do Guia Prático
│   ├── guia_pratico_efd_icms_ipi.pdf
│── output/                # Pasta para salvar as regras extraídas
│   ├── regras_extraidas.json
│── src/                   # Código-fonte do projeto
│   ├── extrair_texto.py   # Extração do texto do PDF
│   ├── extrair_regras.py  # Identifica e organiza regras
│   ├── modelo_ia.py       # IA para validação dos registros
│── requirements.txt       # Dependências do projeto
│── README.md              # Documentação do projeto
```

## Configuração do Ambiente

### 1️⃣ Criar e ativar o ambiente virtual

Execute os comandos abaixo no terminal:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 2️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

Se o arquivo `requirements.txt` ainda não existir, instale as dependências manualmente:

```bash
pip install pymupdf pdfplumber pandas spacy
python -m spacy download pt_core_news_sm
```

## Execução do Projeto

### 1️⃣ Extração do Texto do PDF

```bash
python src/extrair_texto.py
```

Isso gerará um arquivo `output/texto_extraido.txt` contendo o texto extraído do Guia Prático.

### 2️⃣ Extração e Estruturação das Regras

```bash
python src/extrair_regras.py
```

Isso gerará um arquivo `output/regras_extraidas.json` com as regras extraídas dos registros 0200 e 0205.

### 3️⃣ Validação de Registros com IA

```bash
python src/modelo_ia.py
```

Esse script treinará um modelo para detectar erros nos registros de clientes.

## Autor

**Carla Reis** - Trabalho de Conclusão de Curso (TCC) - 2025
