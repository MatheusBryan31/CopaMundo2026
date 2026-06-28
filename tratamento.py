import pandas as pd

# =============================================================
# FUNÇÕES AUXILIARES
# =============================================================
def encontrar_final(copa):
    for partida in copa["matches"]:
        if partida["round"] == "Final":
            return partida



def obter_campeao(final):
    gols_time1 = final["score"]["ft"][0]
    gols_time2 = final["score"]["ft"][1]

    if gols_time1 > gols_time2:
        return final["team1"]
    return final["team2"]



def obter_vice(final):
    gols_time1 = final["score"]["ft"][0]
    gols_time2 = final["score"]["ft"][1]

    if gols_time1 > gols_time2:
        return final["team2"]
    return final["team1"]



def contar_jogos(copa):
    return len(copa["matches"])



def obter_total_gols(copa):
    total_gols = 0
    for partida in copa["matches"]:
        gols_time1 = partida["score"]["ft"][0]
        gols_time2 = partida["score"]["ft"][1]
        total_gols += gols_time1 + gols_time2
    return total_gols



def calcular_media(total_gols, quantidade_jogos):
    return round(total_gols/quantidade_jogos, 2)



def contar_selecoes(copa):
    selecoes = set()

    for partida in copa["matches"]:
        selecoes.add(partida["team1"])
        selecoes.add(partida["team2"])
    return len(selecoes)



# =============================================================
# TRATAMENTO DOS DADOS
# =============================================================
def tratar_dados(copas):
    lista = []

    for copa in copas:
        final = encontrar_final(copa)
        campeao = obter_campeao(final)
        vice = obter_vice(final)
        jogos = contar_jogos(copa)
        total_gols = obter_total_gols(copa)
        media = calcular_media(total_gols, jogos)
        selecoes = contar_selecoes(copa)
        
        lista.append({
            "Ano": int(copa["name"][-4:]),
            "Nome": copa["name"],
            "Campeão": campeao,
            "Vice": vice,
            "Jogos": jogos,
            "Gols": total_gols,
            "Media de Gols": media,
            "Seleções": selecoes
        })
    df = pd.DataFrame(lista)
    return df