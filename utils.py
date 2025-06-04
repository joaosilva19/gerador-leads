import pandas as pd

def salvar_csv(df):
    df.to_csv("leads.csv", index=False)
