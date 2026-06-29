import streamlit as st

# =============================================================
# ARQUIVO DOS FILTROS
# =============================================================
def aplicar_filtros(df):
    st.sidebar.header("Filtros")
    # =============================
    # Ano
    # =============================
    anos = ["Todos"] + sorted(df["Ano"].unique().tolist())
    ano = st.sidebar.selectbox(
        "Ano",
        anos
    )
    # =============================
    # Campeão
    # =============================
    campeoes = ["Todos"] + sorted(df["Campeão"].unique().tolist())
    campeao = st.sidebar.selectbox(
        "Campeão",
        campeoes
    )
    # =============================
    # Sede
    # =============================
    sedes = ["Todas"] + sorted(df["Sede"].unique().tolist())
    sede = st.sidebar.selectbox(
        "Sede",
        sedes
    )
    # =============================
    # Aplicação dos filtros
    # =============================
    df_filtrado = df.copy()
    if ano != "Todos":
        df_filtrado = df_filtrado[df_filtrado["Ano"] == ano]
    if campeao != "Todos":
        df_filtrado = df_filtrado[df_filtrado["Campeão"] == campeao]
    if sede != "Todas":
        df_filtrado = df_filtrado[df_filtrado["Sede"] == sede]
    return df_filtrado