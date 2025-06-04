def enriquecer_leads(df):
    contatos = {
        "TechLorena": "contato@techlorena.com",
        "EducaVale": "contato@educavale.com",
        "Comercial SP": "contato@comercialsp.com"
    }
    df["Contato"] = df["Empresa"].map(contatos)
    return df
