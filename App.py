import streamlit as st
import pandas as pd
import plotly.express as px
from utils import carregar_css
from carregar_dados import carregar_dados
from tratamento import tratar_dados



# =============================================================
# INTERFACE DO PROJETO
#   Arquivo principal, cuja função é unir todo o projeto e or-
#   ganizar de forma clara e objetiva todas as informações que
#   os dados exprimem sobre a as Copas do Mundo da FIFA.
# =============================================================



st.set_page_config(
    page_title="Copas Dashboard",
    page_icon="⚽",
    layout="wide"
)



# =============================================================
# Estilo CSS
# =============================================================
carregar_css("style.css")



# =============================================================
# Load de dados
# =============================================================
copas = carregar_dados()



# =============================================================
# CABECALHO DO DASHBOARD
# =============================================================
st.markdown("# Copas do Mundo Dashboard")
st.markdown("**Explorando os dados históricos da Copa do Mundo da FIFA de 1930 até 2026**")
st.markdown("---")

df = tratar_dados(copas)
st.dataframe(df)

st.sidebar.markdown("## Filtros")
st.sidebar.markdown("Use os filtros abaixo para explorar os dados:")