import pandas as pd

# =============================================================
# ARQUIVO PARA TRATAMENTO DOS DADOS
# =============================================================

def tratar_dados(copas):
    lista = []

    for copa in copas:
        lista.append({
            "Ano": int(copa["name"][-4:]),
            "Nome": copa["name"],
            "Jogos": len(copa["matches"])
        })
    df = pd.DataFrame(lista)
    return df