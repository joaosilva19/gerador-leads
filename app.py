import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

st.set_page_config(page_title="Gerador de Leads", layout="centered")

st.title("🔍 Gerador de Leads")
st.markdown("Este é um gerador automático de leads baseado em filtros definidos.")

cidade = st.selectbox("Selecione a cidade", ["Lorena-SP", "Guaratinguetá-SP", "Aparecida-SP"])
setor = st.selectbox("Selecione o setor", ["Indústria", "Comércio", "Serviços"])

if st.button("🔍 Buscar Leads"):
    with st.spinner("Buscando empresas no Google Maps..."):
        query = f"{setor} em {cidade}"
        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        driver.get(f"https://www.google.com/maps/search/{query}")

        time.sleep(5)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        driver.quit()

        # Coleta simplificada de nomes de empresas (ideal para testar antes de escalar)
        empresas = list(set([tag.text for tag in soup.find_all("div") if tag.text.strip() != ""]))[:5]

    leads = []

    for empresa in empresas:
        try:
            response = requests.get(f"https://publica.cnpj.io/api/cnpj?q={empresa}")
            if response.status_code == 200:
                data = response.json()
                leads.append({
                    "Empresa": data.get("razao_social", empresa),
                    "CNPJ": data.get("cnpj_raiz", ""),
                    "Setor": setor,
                    "Cidade": cidade,
                    "Email": data.get("email", ""),
                    "Telefone": data.get("ddd_telefone_1", ""),
                    "Endereço": data.get("logradouro", "")
                })
        except Exception:
            continue

    df = pd.DataFrame(leads)
    if not df.empty:
        st.success(f"{len(df)} leads encontrados!")
        st.dataframe(df)
        st.download_button("📥 Baixar CSV", data=df.to_csv(index=False), file_name="leads.csv", mime="text/csv")
    else:
        st.warning("Nenhuma empresa encontrada ou API não respondeu.")