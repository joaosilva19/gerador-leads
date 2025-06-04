import streamlit as st
import pandas as pd

st.set_page_config(page_title="Gerador de Leads", layout="centered")

st.title("🧲 Gerador de Leads")
st.markdown("Este é um gerador automático de leads baseado em filtros definidos.")

# Filtros simulados
cidade = st.selectbox("Selecione a cidade", ["Lorena-SP", "Guaratinguetá-SP", "Aparecida-SP"])
setor = st.selectbox("Selecione o setor", ["Tecnologia", "Educação", "Comércio", "Indústria"])

if st.button("🔍 Buscar Leads"):
    # Exemplo de leads simulados
    dados = {
        "Empresa": ["TechLorena", "EducaVale", "Comercial SP"],
        "Setor": [setor]*3,
        "Cidade": [cidade]*3,
        "Contato": ["contato@techlorena.com", "contato@educavale.com", "contato@comercialsp.com"]
    }
    df = pd.DataFrame(dados)
    st.success(f"{len(df)} leads encontrados:")
    st.dataframe(df)
    st.download_button("📥 Baixar CSV", data=df.to_csv(index=False), file_name="leads.csv", mime="text/csv")
