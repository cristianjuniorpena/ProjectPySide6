import requests

def request_cnpj(cnpj, token):
    url = f"https://receitaws.com.br/v1/cnpj/{cnpj}"
    querystring = {
        "token" : token,
        "plugin" : "RF"
    }
    try:
        res = requests.get(url, params=querystring, timeout=10)
        if res.status_code == 429:
            return (False, 'a api de requisições tem um limite de 3 autocomplete por minuto, aguarde um instante e tente novamente')
        res.raise_for_status()
        dados = res.json()
    except requests.exceptions.RequestException as error:
        return (False, f'falha na requisição do cnpj: {error}')

    if dados.get('status') == 'ERROR':
        return (False, dados.get('message', 'a api retornou um erro para este cnpj'))

    return (True, dados)
