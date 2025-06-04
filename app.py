import streamlit as st
from src.scraper import buscar_leads
from src.utils import salvar_csv

st.set_page_config(page_title="Gerador de Leads", page_icon="🔍")
st.title("🔍 Gerador de Leads")
st.write("Este é um gerador automático de leads baseado em filtros definidos.")

cidade = st.selectbox("Selecione a cidade", ["Lorena-SP", "Guaratinguetá-SP", "Aparecida-SP"])
setor = st.selectbox("Selecione o setor", ["Indústria", "Comércio", "Serviços"])

if st.button("🔎 Buscar Leads"):
    leads = buscar_leads(cidade, setor)
    if leads:
        st.success(f"{len(leads)} leads encontrados:")
        st.dataframe(leads)
        salvar_csv(leads, "leads.csv")
        with open("leads.csv", "rb") as f:
            st.download_button("📥 Baixar CSV", f, "leads.csv")
    else:
        st.warning("Nenhum lead encontrado.")