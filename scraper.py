import requests
from bs4 import BeautifulSoup
import pandas as pd
from src.enriquecedor import enriquecer_dados

def buscar_leads(cidade, setor):
    url_base = "https://www.telelistas.net"
    busca = f"{setor}+em+{cidade.replace('-', '+')}".lower().replace(' ', '+')
    url = f"{url_base}/buscar?what={busca}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    empresas_html = soup.select(".resultado-item")

    dados = []
    for item in empresas_html:
        nome = item.select_one(".title")
        contato = item.select_one(".text.tel")
        if nome:
            empresa = nome.get_text(strip=True)
            email = contato.get_text(strip=True) if contato else "Não disponível"
            dados.append({"Empresa": empresa, "Setor": setor, "Cidade": cidade, "Contato": email})

    df = pd.DataFrame(dados)
    return enriquecer_dados(df)
