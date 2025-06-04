import pandas as pd

def buscar_leads(cidade, setor):
    # Simulação: gerar 3 empresas com base nos filtros
    return pd.DataFrame([
        {"Empresa": "TechLorena", "Setor": setor, "Cidade": cidade},
        {"Empresa": "EducaVale", "Setor": setor, "Cidade": cidade},
        {"Empresa": "Comercial SP", "Setor": setor, "Cidade": cidade},
    ])
