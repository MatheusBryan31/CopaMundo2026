import pandas as pd


# =============================================================
# FINAL DA COPA
# =============================================================
def encontrar_final(copa):

    for partida in copa["matches"]:

        if "final" in partida["round"].lower():

            if "score" in partida:
                return partida

    return None


# =============================================================
# CAMPEÃO
# =============================================================
def obter_campeao(final):

    score = final["score"]

    # Tempo normal
    gols1 = score["ft"][0]
    gols2 = score["ft"][1]

    if gols1 > gols2:
        return final["team1"]

    if gols2 > gols1:
        return final["team2"]

    # Prorrogação
    if "et" in score:

        et1 = score["et"][0]
        et2 = score["et"][1]

        if et1 > et2:
            return final["team1"]

        if et2 > et1:
            return final["team2"]

    # Pênaltis
    if "p" in score:

        p1 = score["p"][0]
        p2 = score["p"][1]

        if p1 > p2:
            return final["team1"]

        return final["team2"]

    return "-"


# =============================================================
# VICE
# =============================================================
def obter_vice(final):

    score = final["score"]

    gols1 = score["ft"][0]
    gols2 = score["ft"][1]

    if gols1 > gols2:
        return final["team2"]

    if gols2 > gols1:
        return final["team1"]

    if "et" in score:

        et1 = score["et"][0]
        et2 = score["et"][1]

        if et1 > et2:
            return final["team2"]

        if et2 > et1:
            return final["team1"]

    if "p" in score:

        p1 = score["p"][0]
        p2 = score["p"][1]

        if p1 > p2:
            return final["team2"]

        return final["team1"]

    return "-"


# =============================================================
# COPA DE 1950
# =============================================================
def calcular_classificacao_1950(copa):

    tabela = {}

    for partida in copa["matches"]:

        if partida["round"] != "Final Round":
            continue

        if "score" not in partida:
            continue

        t1 = partida["team1"]
        t2 = partida["team2"]

        g1 = partida["score"]["ft"][0]
        g2 = partida["score"]["ft"][1]

        for time in [t1, t2]:

            if time not in tabela:

                tabela[time] = {

                    "Pontos": 0,
                    "Saldo": 0,
                    "Gols": 0

                }

        tabela[t1]["Gols"] += g1
        tabela[t2]["Gols"] += g2

        tabela[t1]["Saldo"] += g1 - g2
        tabela[t2]["Saldo"] += g2 - g1

        if g1 > g2:

            tabela[t1]["Pontos"] += 2

        elif g2 > g1:

            tabela[t2]["Pontos"] += 2

        else:

            tabela[t1]["Pontos"] += 1
            tabela[t2]["Pontos"] += 1

    return tabela


def obter_campeao_1950(copa):

    tabela = calcular_classificacao_1950(copa)

    classificacao = sorted(

        tabela.items(),

        key=lambda x: (

            x[1]["Pontos"],
            x[1]["Saldo"],
            x[1]["Gols"]

        ),

        reverse=True

    )

    return classificacao[0][0]


def obter_vice_1950(copa):

    tabela = calcular_classificacao_1950(copa)

    classificacao = sorted(

        tabela.items(),

        key=lambda x: (

            x[1]["Pontos"],
            x[1]["Saldo"],
            x[1]["Gols"]

        ),

        reverse=True

    )

    return classificacao[1][0]


# =============================================================
# ESTATÍSTICAS
# =============================================================
def contar_jogos(copa):

    return len(copa["matches"])


def obter_total_gols(copa):

    total = 0

    for partida in copa["matches"]:

        if "score" not in partida:
            continue

        if "ft" not in partida["score"]:
            continue

        total += partida["score"]["ft"][0]
        total += partida["score"]["ft"][1]

    return total


def calcular_media(gols, jogos):

    if jogos == 0:
        return 0

    return round(gols / jogos, 2)


def contar_selecoes(copa):

    selecoes = set()

    for partida in copa["matches"]:

        selecoes.add(partida["team1"])
        selecoes.add(partida["team2"])

    return len(selecoes)