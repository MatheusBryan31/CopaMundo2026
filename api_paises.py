import requests
# Não há mais necessidade de usar este arquivo, todavia, por enquanto, vou deixá-lo aqui.
# =============================================================
# ARQUIVO PARA CONSULTAR DADOS DOS PAÍSES NA API
# =============================================================
URL_API = "https://restcountries.com/v3.1/name/"



def consultar_pais(nome_pais):
    url = URL_API + nome_pais
    resposta = requests.get(url)

    if resposta.status_code == 200:
        return resposta.json()[0]
    
    return None



# =============================================================
# TESTE DO ARQUIVO
# =============================================================
if __name__ == "__main__":
    pais = consultar_pais("Brazil")
    print(pais)    