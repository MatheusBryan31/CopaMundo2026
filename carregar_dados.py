import requests

# =============================================================
# ARQUIVO PARA CARREGAMENTO DOS DADOS
# =============================================================

# URL dos arquivos JSON no GitHub
def carregar_dados():
    anos = range(1930, 2027, 4)
    copas = []

    for ano in anos:
        if ano in [1942, 1946]:
            continue

        URL_DADOS = f"https://raw.githubusercontent.com/openfootball/worldcup.json/refs/heads/master/{ano}/worldcup.json"

        dados = requests.get(URL_DADOS).json()

        copas.append(dados)
    return copas

if __name__ == "__main__":

    copas = carregar_dados()

    print(f"Foram carregadas {len(copas)} Copas.")

    for copa in copas:
        print(copa['name'])