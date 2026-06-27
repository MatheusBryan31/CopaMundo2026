import streamlit as st
import pandas as pd
import plotly.express as px
from utils import carregar_css
from carregar_dados import carregar_dados
from tratamento import tratar_dados



st.set_page_config(
    page_title="Copas Dashboard",
    page_icon="⚽",
    layout="wide"
)



# ----------------------------------------------------------------
# Estilo CSS
# ----------------------------------------------------------------
carregar_css("style.css")



# ----------------------------------------------------------------
# Load de dados
# ----------------------------------------------------------------
copas = carregar_dados()


# =============================================================
# CABECALHO DO DASHBOARD
# =============================================================
st.markdown("# Spotify Streaming Dashboard")
st.markdown("**Explorando os dados de streaming do Spotify entre 2010 e 2019**")
st.markdown("---")

df = tratar_dados(copas)
st.dataframe(df)

st.sidebar.markdown("## Filtros")
st.sidebar.markdown("Use os filtros abaixo para explorar os dados:")