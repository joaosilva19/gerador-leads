import re
import requests
from bs4 import BeautifulSoup

def extrair_emails(texto):
    return re.findall(r"[\w\.-]+@[\w\.-]+", texto)

def extrair_telefones(texto):
    return re.findall(r"(\(?\d{2}\)?\s*\d{4,5}-?\d{4})", texto)

def enriquecer_dados(df):
    headers = {"User-Agent": "Mozilla/5.0"}
    emails, telefones = [], []
    for url in df["url"]:
        try:
            html = requests.get(url, headers=headers, timeout=10).text
            soup = BeautifulSoup(html, "html.parser")
            texto = soup.get_text()
            email = ", ".join(set(extrair_emails(texto))) or "Não encontrado"
            telefone = ", ".join(set(extrair_telefones(texto))) or "Não encontrado"
        except:
            email = "Erro"
            telefone = "Erro"
        emails.append(email)
        telefones.append(telefone)
    
    df["email"] = emails
    df["telefone"] = telefones
    return df[["empresa", "setor", "cidade", "email", "telefone"]]