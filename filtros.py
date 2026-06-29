import streamlit as st

# =============================================================
# FILTROS DO DASHBOARD
# =============================================================
def aplicar_filtros(df):
    st.sidebar.markdown("## Filtros")
    st.sidebar.markdown(
        "Utilize os filtros abaixo para explorar os dados."
    )
    
    # =============================================================
    # FILTRO POR ANO
    # =============================================================
    anos = sorted(df["Ano"].unique())
    anos_selecionados = st.sidebar.multiselect(
        "Ano",
        options = anos,
        default = anos
    )

    # =============================================================
    # FILTRO POR CAMPEÃO
    # =============================================================
    campeoes = sorted(df["Campeão"].unique())
    campeoes_selecionados = st.sidebar.multiselect(
        "Campeão",
        options = campeoes,
        default = campeoes
    )

    # =============================================================
    # FILTRO POR SEDE
    # =============================================================
    sedes = sorted(df["Sede"].unique())
    sedes_selecionadas = st.sidebar.multiselect(
        "País sede",
        options = sedes,
        default = sedes
    )

    # =============================================================
    # APLICAÇÃO DOS FILTROS
    # =============================================================
    df_filtrado = df.copy()
    df_filtrado = df_filtrado[
        df_filtrado["Ano"].isin(anos_selecionados)
    ]
    df_filtrado = df_filtrado[
        df_filtrado["Campeão"].isin(campeoes_selecionados)
    ]
    df_filtrado = df_filtrado[
        df_filtrado["Sede"].isin(sedes_selecionadas)
    ]
    return df_filtrado

    # =============================================================
    # FILTRO POR VICE-CAPEÃO
    # =============================================================
    vices = sorted(df["Vice"].unique())
    vices_selecionados = st.sidebar.multiselect(
        "Vice-campeão",
        options = vices,
        default = vices
    )
    df_filtrado = df_filtrado[
        df_filtrado["Vice"].isin(vices_selecionados)
    ]