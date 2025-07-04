import streamlit as st
import pandas as pd
import os

pasta_processed = '../datalake-bancocentral/lake/processed'
arquivos_csv = sorted([f for f in os.listdir(pasta_processed) if f.endswith('.csv')], reverse=True)

if not arquivos_csv:
    st.error("Nenhum dado processado encontrado.")
else:
    arquivo_mais_recente = os.path.join(pasta_processed, arquivos_csv[0])
    
    
    df = pd.read_csv(arquivo_mais_recente)
    df['data'] = pd.to_datetime(df['data'])

    st.title("📊 Reservas Internacionais - Banco Central do Brasil")
    st.caption("Fonte: [Banco Central - API SGS 1783](https://api.bcb.gov.br/dados/serie/bcdata.sgs.1783/dados)")

    st.subheader("🔍 Dados processados")
    st.dataframe(df)

    st.subheader("📈 Evolução das Reservas Internacionais")
    st.line_chart(df.set_index('data')['valor'])

    st.success(f"Dados carregados de: `{arquivo_mais_recente}`")
