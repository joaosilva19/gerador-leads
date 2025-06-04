
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Gerador de Leads", layout="wide")

st.title("🚀 Gerador Inteligente de Leads")
st.markdown("Use os filtros abaixo para buscar empresas e responsáveis automaticamente.")

# Filtros de entrada
with st.sidebar:
    st.header("Filtros")
    cidade = st.text_input("Cidade", value="Lorena-SP")
    setor = st.selectbox("Setor", ["Tecnologia", "Saúde", "Educação", "Financeiro", "Outro"])
    cargo = st.selectbox("Cargo", ["CEO", "Diretor", "Gerente", "Marketing", "Outro"])
    colaboradores = st.slider("Nº de funcionários", 1, 1000, (10, 200))
    buscar = st.button("🔍 Buscar Leads")

if buscar:
    st.info("🔄 Buscando leads com os filtros informados...")
    # Aqui virá o scraping ou chamada à API
    st.success("✅ Busca finalizada!")
    dados = pd.DataFrame({
        "Empresa": ["TechOne", "EduMais"],
        "Responsável": ["João Silva", "Maria Souza"],
        "Cargo": ["CEO", "Diretora"],
        "Localização": ["Lorena-SP", "Lorena-SP"],
        "Setor": ["Tecnologia", "Educação"],
        "Funcionários": [50, 120],
        "LinkedIn": ["https://linkedin.com/in/joaosilva", "https://linkedin.com/in/mariasouza"]
    })
    st.dataframe(dados)
