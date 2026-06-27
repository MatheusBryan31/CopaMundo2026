import streamlit as st
import pandas as pd
import plotly.express as px
from utils import carregar_css
from carregar_dados import carregar_dados



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


# =============================================================
# FILTROS INTERATIVOS (na barra lateral esquerda)
# -------------------------------------------------------------
# No Streamlit, tudo que começa com st.sidebar aparece
# na barra do lado esquerdo da tela.
#
# Filtro 1: Slider de ano   -> o usuario escolhe um intervalo
# Filtro 2: Multiselect     -> o usuario escolhe um ou mais generos
# =============================================================
st.sidebar.markdown("## Filtros")
st.sidebar.markdown("Use os filtros abaixo para explorar os dados:")

# FILTRO 1: Intervalo de anos
# sorted() ordena os anos do menor para o maior
#anos_disponiveis = sorted(df["Year"].dropna().unique())

# int() converte para numero inteiro normal (o pandas usa Int64)
#ano_min = int(min(anos_disponiveis))
#ano_max = int(max(anos_disponiveis))

# st.sidebar.slider cria um controle deslizante com dois pontos
# value=(ano_min, ano_max) significa que começa mostrando todos os anos
#intervalo_ano = st.sidebar.slider(
#    "Ano de lancamento",
#   min_value=ano_min,
#    max_value=ano_max,
#    value=(ano_min, ano_max)
#)

# FILTRO 2: Genero musical
# sorted() ordena os generos em ordem alfabetica
#generos_disponiveis = sorted(df["Genre"].dropna().unique())

# st.sidebar.multiselect cria uma lista onde o usuario pode
# marcar varios itens ao mesmo tempo
# default= define quais generos ja vem selecionados ao abrir
#generos_escolhidos = st.sidebar.multiselect(
#    "Genero musical",
#    options=generos_disponiveis,
#    default=generos_disponiveis[:8]     # começa com os 8 primeiros selecionados
#)

# -------------------------------------------------------------
# APLICACAO DOS FILTROS
# -------------------------------------------------------------
# Aqui criamos um novo dataframe chamado df_filtrado
# que contem SOMENTE as linhas que passam pelos dois filtros.
#
# A condicao funciona assim:
#   (df["Year"] >= intervalo_ano[0])   -> ano maior ou igual ao minimo escolhido
#   (df["Year"] <= intervalo_ano[1])   -> ano menor ou igual ao maximo escolhido
#   (df["Genre"].isin(generos_escolhidos)) -> genero esta na lista selecionada
#
# O operador & significa "E" (todas as condicoes devem ser verdadeiras)
# -------------------------------------------------------------
#df_filtrado = df[
#    (df["Year"] >= intervalo_ano[0]) &
#    (df["Year"] <= intervalo_ano[1]) &
#    (df["Genre"].isin(generos_escolhidos))
#]

# Mostra na barra lateral quantas musicas foram encontradas
st.sidebar.markdown("---")
st.sidebar.markdown(f"**{len(df_filtrado):,} musicas** encontradas com esses filtros.")


# =============================================================
# KPIs - INDICADORES NUMERICOS EM DESTAQUE
# Os KPIs sao calculados com base nos dados filtrados (df_filtrado)
# Entao eles mudam automaticamente quando o usuario mexe nos filtros
# =============================================================
#st.markdown("### Indicadores Gerais")

#col1, col2, col3 = st.columns(3)   # divide a linha em 3 colunas iguais

# KPI 1: Total de streams
#total_streams = df_filtrado["Streams"].sum()
