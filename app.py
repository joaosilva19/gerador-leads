import streamlit as st
import pandas as pd
from scraper import buscar_leads
from enriquecedor import enriquecer_dados

st.set_page_config(page_title="Gerador de Leads", page_icon="🔍")
st.title("🔍 Gerador de Leads")
st.write("Este é um gerador automático de leads baseado em filtros definidos.")

cidade = st.selectbox("Selecione a cidade", ["Lorena-SP", "Guaratinguetá-SP", "Aparecida-SP"])
setor = st.selectbox("Selecione o setor", ["Indústria", "Comércio", "Educação", "Saúde"])

if st.button("🔎 Buscar Leads"):
    with st.spinner("Buscando leads..."):
        leads_brutos = buscar_leads(cidade, setor)
        leads_enriquecidos = enriquecer_dados(leads_brutos)
        st.success(f"{len(leads_enriquecidos)} leads encontrados:")
        st.dataframe(leads_enriquecidos)
        csv = leads_enriquecidos.to_csv(index=False).encode("utf-8")
        st.download_button("📥 Baixar CSV", csv, "leads.csv", "text/csv")