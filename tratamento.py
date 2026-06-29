import os
import pandas as pd
from funcoes import *

# =============================================================
# ARQUIVO PARA TRATAMENTO DOS DADOS
# =============================================================
CAMINHO_SEDES = os.path.join("Data", "sedes.csv")
df_sedes = pd.read_csv(
    CAMINHO_SEDES,
    sep=";"
)



# =============================================================
# TRATAMENTO DO CSV
# =============================================================
def obter_sede(ano):
    resultado = df_sedes.loc[
        df_sedes["Ano"] == ano,
        "Pais_Sede"
    ]
    if resultado.empty:
        return "-"
    return resultado.iloc[0]



# =============================================================
# TRATAMENDO DOS DADOS
# =============================================================
def tratar_dados(copas):
    lista = []

    for copa in copas:
        ano = int(copa["name"][-4:])
        sede = obter_sede(ano)

        if ano == 1950:
            campeao = obter_campeao_1950(copa)
            vice = obter_vice_1950(copa)
        else:
            final = encontrar_final(copa)

            if final is None:
                campeao = "-"
                vice = "-"
            else:
                campeao = obter_campeao(final)
                vice = obter_vice(final)
        jogos = contar_jogos(copa)
        gols = obter_total_gols(copa)
        media = calcular_media(gols, jogos)
        selecoes = contar_selecoes(copa)
        lista.append({
            "Ano": ano,
            "Nome": copa["name"],
            "Sede": sede,
            "Campeão": campeao,
            "Vice": vice,
            "Jogos": jogos,
            "Gols": gols,
            "Média de Gols": media,
            "Seleções": selecoes
        })
    return pd.DataFrame(lista)