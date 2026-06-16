import requests
import json

from conn.config import URL, TOKEN

headers = {'x-token': TOKEN}


def make_request(type, api_url, payload=None):
    if not URL or not TOKEN:
        return "Configuração ausente: defina URL e TOKEN (env, .env ou var/token.py)."
    try:
        response = requests.request(type, api_url, headers=headers, data=payload)
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            return f"Erro na chamada de API (status code {response.status_code})."
    except requests.RequestException as e:
            return  f"Erro na chamada de API: {e}"

def put_products(payload):
    api_url = URL + '/surprise-produtos'
    return make_request('POST', api_url, payload)

def put_respostas(payload):
    api_url = URL + '/surprise-respostas'
    return make_request('POST', api_url, payload)

def get_all_products():
    api_url = URL + '/surprise-produtos?idProduto=all'
    return make_request('GET', api_url)

def get_all_respostas():
    api_url = URL + '/surprise-respostas?idResposta=all'
    return make_request('GET', api_url)

def post_predict(filebase64):
    api_url = URL + '/surprise-predict'
    payload = json.dumps({'file' : filebase64 })
    return make_request('POST', api_url, payload)

def get_predict():
    api_url = URL + '/surprise-predict'
    return make_request('GET', api_url)
