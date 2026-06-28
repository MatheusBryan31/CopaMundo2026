import os
import pandas as pd



# =============================================================
# LEITURA DAS SEDES
# =============================================================
CAMINHO_SEDES = os.path.join("Data", "sedes.csv")

df_sedes = pd.read_csv(
    CAMINHO_SEDES,
    sep=";"
)



# =============================================================
# FUNÇÕES AUXILIARES
#   Funções do arquivo:
#       ├── encontrar_final()
#       ├── obter_campeao()
#       ├── obter_vice()
#       ├── calcular_classificacao_1950()   
#       ├── obter_campeao_1950()            
#       ├── obter_vice_1950()               
#       ├── contar_jogos()
#       ├── obter_total_gols()
#       ├── calcular_media()
#       ├── contar_selecoes()
#       ├── obter_sede()
#       └── tratar_dados() -> Não é função auxiliar, apenas reune todas as funções e organiza a interface
# =============================================================
def encontrar_final(copa):
    for partida in copa["matches"]:
        if partida["round"] == "Final":
            if "score" in partida:
                return partida
    return None



def obter_campeao(final):
    score = final["score"]

    # Tempo normal
    gols_time1 = score["ft"][0]
    gols_time2 = score["ft"][1]

    if gols_time1 > gols_time2:
        return final["team1"]
    
    if gols_time2 > gols_time1:
        return final["team2"]
    
    # EMPATE TEMPO NORMAL = Prorrogação:
    if "et" in score:
        gols_time1 = score["et"][0]
        gols_time2 = score["et"][1]

        if gols_time1 > gols_time2:
            return final["team1"]
        
        if gols_time2 > gols_time1:
            return final["team2"]

    # EMPATE PRORROGAÇÃO = Pênaltis:
    if "p" in score:
        pen_time1 = score["p"][0]
        pen_time2 = score["p"][1]

        if pen_time1 > pen_time2:
            return final["team1"]
        
        return final["team2"]
    return "-"



def obter_vice(final):
    gols_time1 = final["score"]["ft"][0]
    gols_time2 = final["score"]["ft"][1]

    if gols_time1 > gols_time2:
        return final["team2"]
    return final["team1"]



def calcular_classificacao_1950(copa):
    tabela = {}

    for partida in copa["matches"]:
        if partida["round"] != "Final Round":
            continue
        if "score" not in partida:
            continue

        time1 = partida["team1"]
        time2 = partida["team2"]

        gols1 = partida["score"]["ft"][0]
        gols2 = partida["score"]["ft"][1]
        
        # Inicializa os times na tabela
        for time in [time1, time2]:
            if time not in tabela:
                tabela[time] = {
                    "Pontos":0,
                    "Saldo":0,
                    "Gols":0
                }
        # Soma gols marcados
        tabela[time1]["Gols"] += gols1
        tabela[time2]["Gols"] += gols2

        # Soma Saldo
        tabela[time1]["Saldo"] += gols1 - gols2
        tabela[time2]["Saldo"] += gols2 - gols1

        # Vitória
        if gols1 > gols2:
            tabela[time1]["Pontos"] += 2

        elif gols2 > gols1:
            tabela[time2]["Pontos"] += 2

        # Empate
        else:
            tabela[time1]["Pontos"] += 1
            tabela[time2]["Pontos"] += 1
    return tabela



def obter_campeao_1950(copa):
    tabela = calcular_classificacao_1950(copa)
    classificacao = sorted(
        tabela.items(),
        key=lambda item: (
            item[1]["Pontos"],
            item[1]["Saldo"],
            item[1]["Gols"]
        ),
        reverse = True
    )
    return classificacao[0][0]



def obter_vice_1950(copa):
    tabela = calcular_classificacao_1950(copa)
    classificacao = sorted(
        tabela.items(),
        key=lambda item: (
            item[1]["Pontos"],
            item[1]["Saldo"],
            item[1]["Gols"]
        ),
        reverse = True
    )
    return classificacao[1][0]



def contar_jogos(copa):
    return len(copa["matches"])



def obter_total_gols(copa):
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
    if quantidade_jogos == 0:
        return 0
    return round(total_gols / quantidade_jogos, 2)



def contar_selecoes(copa):
    selecoes = set()

    for partida in copa["matches"]:
        selecoes.add(partida["team1"])
        selecoes.add(partida["team2"])
    return len(selecoes)



def obter_sede(ano):
    resultado = df_sedes.loc[
        df_sedes["Ano"] == ano,
        "Pais_Sede"
    ]

    if resultado.empty:
        return "-" 
    return resultado.iloc[0]



# =============================================================
# TRATAMENTO DOS DADOS
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
        total_gols = obter_total_gols(copa)
        media = calcular_media(total_gols, jogos)
        selecoes = contar_selecoes(copa)
        lista.append({

            "Ano": ano,

            "Nome": copa["name"],

            "Sede": sede,

            "Campeão": campeao,

            "Vice": vice,

            "Jogos": jogos,

            "Gols": total_gols,

            "Média de Gols": media,

            "Seleções": selecoes

        })
    df = pd.DataFrame(lista)
    return df