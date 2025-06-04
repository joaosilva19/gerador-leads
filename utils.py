import streamlit as st

def baixar_csv(df):
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Baixar CSV", csv, "leads.csv", "text/csv")
