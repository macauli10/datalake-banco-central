import pandas as pd
import json
import os
from datetime import datetime


hoje = datetime.today().strftime('%Y-%m-%d')
arquivo_raw = f'../datalake-bancocentral/lake/raw/reservas_internacionais_{hoje}.json'
os.makedirs('../datalake-bancocentral/lake/processed', exist_ok=True)
arquivo_processed = f'../datalake-bancocentral/lake/processed/reservas_internacionais_{hoje}.csv'

with open(arquivo_raw, 'r', encoding='utf-8') as f:
    dados = json.load(f)


df = pd.DataFrame(dados)
df['valor'] = pd.to_numeric(df['valor'], errors='coerce')
df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')
df.to_csv(arquivo_processed, index=False)

print(f"✅ Dados processados salvos em CSV na Processed Zone: {arquivo_processed}")