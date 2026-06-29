import streamlit as st
import plotly.express as px

# =============================================================
# GRÁFICOS
#   Arquivo responsável pela construção de todos os gráficos
#   apresentados no Dashboard.
#
#   Funções:
#       ├── grafico_campeoes()
#       ├── grafico_gols()
#       ├── grafico_media_gols()
#       ├── grafico_jogos()
#       ├── grafico_selecoes()
#       ├── grafico_sedes()
#       └── exibir_graficos()
# =============================================================

# Primeiro gráfico
def grafico_campeoes(df):

    titulos = (
        df[df["Campeão"] != "-"]
        ["Campeão"]
        .value_counts()
        .reset_index()
    )

    titulos.columns = [
        "País",
        "Títulos"
    ]

    fig = px.bar(

        titulos,

        x="País",

        y="Títulos",

        title="Títulos por Seleção",

        text="Títulos"

    )

    fig.update_layout(

        title_x=0.5,

        xaxis_title="Seleção",

        yaxis_title="Quantidade"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )



# Segundo gráfico
def grafico_gols(df):

    fig = px.line(

        df,

        x="Ano",

        y="Gols",

        markers=True,

        title="Total de Gols por Copa"

    )

    fig.update_layout(

        title_x=0.5,

        xaxis_title="Ano",

        yaxis_title="Gols"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )



# Terceiro gráfico
def grafico_media_gols(df):

    fig = px.line(

        df,

        x="Ano",

        y="Média de Gols",

        markers=True,

        title="Média de Gols por Jogo"

    )

    fig.update_layout(

        title_x=0.5,

        xaxis_title="Ano",

        yaxis_title="Média"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )



# Quarto gráfico
def grafico_jogos(df):

    fig = px.bar(

        df,

        x="Ano",

        y="Jogos",

        title="Quantidade de Jogos"

    )

    fig.update_layout(

        title_x=0.5

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )



# Quinto gráfico
def grafico_selecoes(df):

    fig = px.line(

        df,

        x="Ano",

        y="Seleções",

        markers=True,

        title="Seleções Participantes"

    )

    fig.update_layout(

        title_x=0.5

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )



# Sexto gráfico
def grafico_sedes(df):

    sedes = (

        df["Sede"]

        .value_counts()

        .reset_index()

    )

    sedes.columns = [

        "País",

        "Copas"

    ]

    fig = px.bar(

        sedes,

        x="Copas",

        y="País",

        orientation="h",

        title="Copas Sediadas por País"

    )

    fig.update_layout(

        title_x=0.5

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )



# Exibição dos gráficos
def exibir_graficos(df):

    col1, col2 = st.columns(2)

    with col1:

        grafico_campeoes(df)

    with col2:

        grafico_gols(df)

    col3, col4 = st.columns(2)

    with col3:

        grafico_media_gols(df)

    with col4:

        grafico_jogos(df)

    col5, col6 = st.columns(2)

    with col5:

        grafico_selecoes(df)

    with col6:

        grafico_sedes(df)
