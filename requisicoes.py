import requests
import time

def requestCNPJ(cnpj):
    try:
        url = f"https://receitaws.com.br/v1/cnpj/{cnpj}"
        querystring = {
            "token" : "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
            "plugin" : "RF"
        }    
        res = requests.get(url, params=querystring)
        res.raise_for_status()
        return res.json()
    except requests.exceptions.RequestException as error:
        if res.status_code == 429:
            print("Limite atingido. Aguardando para tentar novamente...")
            time.sleep(20)  # Espera 20 segundos
            return res.json()
        else:
            print(f'{error}')

    