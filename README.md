# 📊 Projeto de Engenharia de Dados: Pipeline de Reservas Internacionais com Data Lake, Streamlit e Docker

Este projeto foi desenvolvido com o objetivo de simular um pipeline de **engenharia de dados completo**, desde a **extração de dados brutos** de uma API pública, até o **armazenamento em Data Lake**, **transformação**, e **visualização interativa** com Streamlit — tudo isso **containerizado com Docker**, para garantir portabilidade e reprodutibilidade do ambiente.

---

## 🚀 Tecnologias Utilizadas

- **Python 3.12**
- **Pandas**
- **Streamlit**
- **Docker**
- **API do Banco Central do Brasil (SGS)**
- **Data Lake (Raw e Processed Zones em arquivos)**
- **CSV e JSON**

---

## 🧱 Arquitetura do Projeto

```plaintext
datalake-bancocentral/
├── lake/
│   ├── raw/               ← Dados brutos (JSON da API)
│   └── processed/         ← Dados tratados (CSV)
├── src/
│   ├── app.py             ← Script de extração e transformação
│   └── dashboard.py       ← Aplicação Streamlit
├── Dockerfile             ← Docker para empacotar o projeto
├── .dockerignore          ← Ignora arquivos desnecessários
└── README.md              ← Documentação
🛠️ Funcionalidades
1. 📡 Extração da API
Os dados são extraídos da API pública do Banco Central do Brasil (SGS) — mais especificamente da série histórica SGS 1783, que representa as reservas internacionais do Brasil em dólares.

python
Copy
Edit
https://api.bcb.gov.br/dados/serie/bcdata.sgs.1783/dados?formato=json
2. 🧊 Armazenamento em Data Lake (Raw Zone)
Após a extração, os dados são armazenados em arquivos JSON na pasta lake/raw/, mantendo o formato original e o histórico diário.

3. 🔁 Processed Zone (Transformação)
O script converte os dados brutos para CSV, trata tipos de dados e armazena na pasta lake/processed/, criando uma camada de dados estruturados pronta para análise.

4. 📈 Visualização com Streamlit
A aplicação dashboard.py consome o CSV da Processed Zone e exibe:

Uma tabela com os dados formatados

Um gráfico de linha com a evolução temporal das reservas

5. 🐳 Dockerização Completa
O projeto é totalmente containerizado. Com Docker instalado, você pode rodá-lo em qualquer máquina com os comandos:

bash
Copy
Edit
docker build -t dashboard-bcb .
docker run -p 8501:8501 dashboard-bcb
Acesse em: http://localhost:8501

📦 Como Executar Localmente (sem Docker)
Clone o projeto:

bash
Copy
Edit
git clone https://github.com/macauli10/datalake-banco-central.git
cd datalake-bancocentral
Crie um ambiente virtual:

bash
Copy
Edit
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
Instale as dependências:

bash
Copy
Edit
pip install -r requirements.txt
Rode o pipeline:

bash
Copy
Edit
python src/app.py
Inicie o dashboard:

bash
Copy
Edit
streamlit run src/dashboard.py
📌 Conclusão
Este projeto demonstra um ciclo completo de engenharia de dados:

Extração automatizada de dados financeiros reais

Armazenamento em camadas de um Data Lake

Transformação estruturada dos dados

Visualização interativa e acessível

Empacotamento com Docker para rodar em qualquer ambiente

Ele serve como base para projetos maiores de dados, podendo ser integrado com bancos relacionais, Airflow, nuvem (AWS S3, GCS), ou ferramentas de modelagem e machine learning.