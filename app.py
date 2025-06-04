import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import quote_plus

# Configurações da página
st.set_page_config(page_title="Gerador de Leads Avançado", layout="wide")
st.title("📈 Gerador de Leads Avançado (Estilo Apollo.io)")

st.markdown("""
Este aplicativo localiza empresas reais por setor e cidade, extrai informações de contato e dados adicionais.
Utiliza scraping de TeleListas para buscar e-mails e telefones.
""")

# Entradas de filtro
with st.sidebar:
    st.header("Filtros de Busca")
    cidade = st.text_input("Cidade", value="Lorena SP")
    setor = st.text_input("Setor/Segmento", value="Indústria")
    num_resultados = st.slider("Número de empresas a buscar", 1, 20, 5)

if st.button("🔎 Buscar Leads"):
    if not cidade or not setor:
        st.warning("Preencha cidade e setor para buscar.")
    else:
        with st.spinner("Buscando empresas..."):
            df_empresas = buscar_companies(cidade, setor, num_resultados)
            if df_empresas.empty:
                st.error("Nenhuma empresa encontrada.")
            else:
                with st.spinner("Enriquecendo dados de contato..."):
                    df_final = enriquecer_dados(df_empresas)
                    st.success(f"{len(df_final)} leads encontrados:")
                    st.dataframe(df_final)
                    csv = df_final.to_csv(index=False).encode("utf-8")
                    st.download_button("📥 Baixar CSV", csv, "leads.csv", "text/csv")

# Função para buscar empresas via Google+TeleListas
def buscar_companies(cidade, setor, limite):
    query = f'setor:{setor} "{cidade}" site:telelistas.net'
    url_busca = f"https://www.google.com/search?q={quote_plus(query)}"
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(url_busca, headers=headers, timeout=10)
    soup = BeautifulSoup(resp.text, "html.parser")
    links = []
    for a in soup.select("a"):
        href = a.get("href")
        if href and "/url?q=" in href and "telelistas.net" in href:
            link = href.split("/url?q=")[1].split("&")[0]
            if link not in links:
                links.append(link)
        if len(links) >= limite:
            break

    dados = []
    for link in links:
        try:
            page = requests.get(link, headers=headers, timeout=10)
            soup_comp = BeautifulSoup(page.text, "html.parser")
            nome = soup_comp.find("h1").get_text(strip=True) if soup_comp.find("h1") else "Nome não disponível"
            dados.append({"empresa": nome, "link": link, "setor": setor, "cidade": cidade})
        except:
            continue

    return pd.DataFrame(dados)

# Função para enriquecer dados com e-mails e telefones
def enriquecer_dados(df):
    emails = []
    telefones = []
    headers = {"User-Agent": "Mozilla/5.0"}
    for idx, row in df.iterrows():
        url = row["link"]
        try:
            resp = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(resp.text, "html.parser")
            texto = soup.get_text(separator=" ", strip=True)
            email_match = re.findall(r"[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}", texto)
            tel_match = re.findall(r"\(?\d{2}\)?\s*\d{4,5}-?\d{4}", texto)
            emails.append(", ".join(set(email_match)) if email_match else "Não encontrado")
            telefones.append(", ".join(set(tel_match)) if tel_match else "Não encontrado")
        except:
            emails.append("Erro ao acessar")
            telefones.append("Erro ao acessar")

    df["email"] = emails
    df["telefone"] = telefones
    # Renomear colunas para estilo Apollo.io
    df = df.rename(columns={
        "empresa": "Empresa",
        "setor": "Setor",
        "cidade": "Cidade",
        "link": "Website"
    })
    return df[["Empresa", "Setor", "Cidade", "Website", "email", "telefone"]]