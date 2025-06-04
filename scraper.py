import requests
from bs4 import BeautifulSoup
import pandas as pd

def buscar_leads(cidade, setor):
    query = f"{setor} {cidade} site:telelistas.net"
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    resultados = []
    for link in soup.select("a"):
        href = link.get("href")
        if href and "http" in href and "telelistas.net" in href:
            resultados.append(href.split("&")[0].replace("/url?q=", ""))
    
    dados = []
    for url in resultados[:5]:
        try:
            page = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(page.text, "html.parser")
            nome = soup.find("h1").text.strip() if soup.find("h1") else "Empresa desconhecida"
            dados.append({"empresa": nome, "url": url, "cidade": cidade, "setor": setor})
        except:
            continue

    return pd.DataFrame(dados)