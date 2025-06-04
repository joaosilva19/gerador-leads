import streamlit as st
import pandas as pd
from src.scraper import buscar_leads
from src.utils import salvar_csv

st.set_page_config(page_title="Gerador de Leads", layout="centered")
st.markdown("## 🔍 Gerador de Leads")
st.markdown("Este é um gerador automático de leads baseado em filtros definidos.")

cidade = st.selectbox("Selecione a cidade", ["Lorena-SP", "Guaratinguetá-SP", "Aparecida-SP"])
setor = st.selectbox("Selecione o setor", ["Indústria", "Comércio", "Serviços"])

if st.button("🔎 Buscar Leads"):
    leads = buscar_leads(cidade, setor)
    if leads.empty:
        st.warning("Nenhum lead encontrado.")
    else:
        st.success(f"{len(leads)} leads encontrados:")
        st.dataframe(leads)
        salvar_csv(leads)
        with open("leads.csv", "rb") as file:
            st.download_button("📥 Baixar CSV", file, "leads.csv", "text/csv")
