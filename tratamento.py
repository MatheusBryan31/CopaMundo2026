import pandas as pd

# =============================================================
# FUNÇÕES AUXILIARES
# =============================================================

def encontrar_final(copa):
    """
    Procura a partida da final.
    Caso a Copa ainda não tenha sido disputada (2026),
    retorna None.
    """

    for partida in copa["matches"]:
        if partida["round"] == "Final":

            # Só retorna se a final possuir placar
            if "score" in partida:
                return partida

    return None


def obter_campeao(final):
    """
    Retorna o campeão da Copa.
    """

    gols_time1 = final["score"]["ft"][0]
    gols_time2 = final["score"]["ft"][1]

    if gols_time1 > gols_time2:
        return final["team1"]

    return final["team2"]


def obter_vice(final):
    """
    Retorna o vice-campeão.
    """

    gols_time1 = final["score"]["ft"][0]
    gols_time2 = final["score"]["ft"][1]

    if gols_time1 > gols_time2:
        return final["team2"]

    return final["team1"]


def contar_jogos(copa):
    """
    Conta o número de partidas cadastradas.
    """

    return len(copa["matches"])


def obter_total_gols(copa):
    """
    Soma todos os gols da Copa.
    Ignora partidas sem resultado (2026).
    """

    total_gols = 0

    for partida in copa["matches"]:

        if "score" not in partida:
            continue

        if "ft" not in partida["score"]:
            continue

        gols_time1 = partida["score"]["ft"][0]
        gols_time2 = partida["score"]["ft"][1]

        total_gols += gols_time1 + gols_time2

    return total_gols


def calcular_media(total_gols, quantidade_jogos):
    """
    Calcula a média de gols.
    """

    if quantidade_jogos == 0:
        return 0

    return round(total_gols / quantidade_jogos, 2)


def contar_selecoes(copa):
    """
    Conta quantas seleções participaram da Copa.
    """

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

        if final is None:
            campeao = "-"
            vice = "-"
        else:
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

            "Média de Gols": media,

            "Seleções": selecoes

        })

    df = pd.DataFrame(lista)

    return df