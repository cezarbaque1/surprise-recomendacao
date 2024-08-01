import requests
import json
import os

if 'URL' in os.environ:
    url = os.getenv('URL')
    headers = json.loads(os.getenv('HEADERS'))
else:
    # Importa todas as variáveis do módulo 'var.token'
    try:
        from var.token import *
        print("Variáveis do módulo 'var.token' foram importadas com sucesso.")
    except ImportError as e:
        print(f"Erro ao importar variáveis do módulo 'var.token': {e}")


def make_request(type, api_url, payload=None):
    try:
        response = requests.request(type, api_url, headers=headers, data=payload)
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            return f"Erro na chamada de API (status code {response.status_code})."
    except requests.RequestException as e:
            return  f"Erro na chamada de API: {e}"

def put_products(payload):
    api_url = url + '/surprise-produtos'
    return make_request('POST', api_url, payload)
    
def put_respostas(payload):
    api_url = url + '/surprise-respostas'
    return make_request('POST', api_url, payload)
    
def get_all_products():
    api_url = url + '/surprise-produtos?idProduto=all'
    return make_request('GET', api_url)