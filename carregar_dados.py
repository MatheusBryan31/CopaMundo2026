import json
import os

# =============================================================
# ARQUIVO PARA CARREGAMENTO DOS DADOS
# =============================================================

PASTA_DADOS = "Data"

def carregar_dados():
    copas = []
    anos = range(1930, 2027, 4)

    for ano in anos:
        if ano in [1942, 1946]:
            continue
        with open(f"{PASTA_DADOS}/{ano}.json", encoding="utf-8") as f:
            copas.append(json.load(f))
        return copas

if __name__ == "__main__":
    copas = carregar_dados()
    print(f"Foram carregadas {len(copas)} Copas.")

    for copa in copas:
        print(copa["name"])