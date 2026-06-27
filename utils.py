import streamlit as st

def carregar_css(nome_arquivo):
    with open(nome_arquivo) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )