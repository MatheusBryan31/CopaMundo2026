import requests

# =============================================================
# ARQUIVO PARA CONSULTAR DADOS DE UM PAÍS NA API
# =============================================================
def consultar_pais(nome_pais):
    url = f"https://restcountries.com/v3.1/name/{nome_pais}"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        return resposta.json()[0]
    return None;