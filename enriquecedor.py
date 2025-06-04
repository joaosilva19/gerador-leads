import pandas as pd
import requests

def enriquecer_dados(df):
    for i, row in df.iterrows():
        cnpj_data = buscar_cnpj(row["Empresa"])
        if cnpj_data:
            df.at[i, "CNPJ"] = cnpj_data.get("estabelecimento", {}).get("cnpj", "")
            df.at[i, "Telefone"] = cnpj_data.get("estabelecimento", {}).get("ddd1", "") + cnpj_data.get("estabelecimento", {}).get("telefone1", "")
    return df

def buscar_cnpj(razao_social):
    try:
        r = requests.get(f"https://publica.cnpj.ws/cnpj/{razao_social}")
        if r.status_code == 200:
            return r.json()
    except:
        return None
