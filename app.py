import streamlit as st
import pandas as pd
from scraper import buscar_leads
from enriquecedor import enriquecer_leads
from utils import baixar_csv

st.set_page_config(page_title="Gerador de Leads", page_icon="🔍")

st.markdown("# 🔍 Gerador de Leads")
st.markdown("Este é um gerador automático de leads baseado em filtros definidos.")

cidade = st.selectbox("Selecione a cidade", ["Lorena-SP"])
setor = st.selectbox("Selecione o setor", ["Indústria", "Comércio", "Serviços", "Tecnologia"])

if st.button("🔎 Buscar Leads"):
    with st.spinner("Buscando empresas..."):
        leads = buscar_leads(cidade, setor)
        leads = enriquecer_leads(leads)
        if not leads.empty:
            st.success(f"{len(leads)} leads encontrados:")
            st.dataframe(leads)
            baixar_csv(leads)
        else:
            st.warning("Nenhum lead encontrado.")
