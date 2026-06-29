import os
import requests

# ===========================================================
# BAIXAR ARQUIVOS JSON DAS COPAS
# ===========================================================
def baixar_json():
    # Cria a pasta "dados" caso ela não exista, porém eu já criei. É apenas para proteção mesmo.
    PASTA_DADOS = "Data"
    os.makedirs(PASTA_DADOS, exist_ok=True)
    anos = range(1930, 2027, 4)

    for ano in anos:
        if ano in [1942, 1946]:
            continue
        url = f"https://raw.githubusercontent.com/openfootball/worldcup.json/master/{ano}/worldcup.json"
        resposta = requests.get(url)

        if resposta.status_code == 200:
            caminho = os.path.join(PASTA_DADOS, f"{ano}.json")

            with open(caminho, "w", encoding="utf-8") as arquivo:
                arquivo.write(resposta.text)
            print(f"✔ Copa {ano} baixada.")
        else:
            print(f"✘ Erro ao baixar arquivo {ano}.")
if __name__ == "__main__":
    baixar_json()