import streamlit as st
import pandas as pd
import plotly.express as px
from utils import carregar_css
from carregar_dados import carregar_dados
from tratamento import tratar_dados
from filtros import aplicar_filtros
from graficos import exibir_graficos

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
df = tratar_dados(copas) # Carrega os dados
df = aplicar_filtros(df) # Carrega os filtros



# =============================================================
# KPIs
# =============================================================
# Considera apenas Copas já encerradas
df_finalizadas = df[df["Campeão"] != "-"]

# Cria três colunas
col1, col2, col3 = st.columns(3)

# KPI 1 - Total de Copas
total_copas = len(df_finalizadas)

# KPI 2 - Total de gols
total_gols = df_finalizadas["Gols"].sum()

# KPI 3 - Maior campeão
titulos = df_finalizadas["Campeão"].value_counts()

maior_campeao = titulos.index[0]
quantidade_titulos = titulos.iloc[0]

with col1:
    st.metric(
        label="🏆 Total de Copas",
        value=total_copas
    )

with col2:
    st.metric(
        label="⚽ Total de Gols",
        value=total_gols
    )

with col3:
    st.metric(
        label="👑 Maior Campeão",
        value=maior_campeao,
        delta=f"{quantidade_titulos} títulos"
    )
st.markdown("---")



# =============================================================
# GRÁFICOS
# =============================================================
st.dataframe(df)
st.markdown("---")
st.subheader("Análises Gráficas")
exibir_graficos(df)



# =============================================================
# TABELA
# =============================================================
st.dataframe(df)

# Restos do código de Suzana

#st.sidebar.markdown("## Filtros")
#st.sidebar.markdown("Use os filtros abaixo para explorar os dados:")