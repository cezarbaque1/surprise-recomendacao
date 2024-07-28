import requests
import json
import var.token
    
def put_products(payload):
    api_url = url + '/surprise-produtos'
    try:
        response = requests.request("POST", api_url, headers=headers, data=payload)
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            return f"Erro na chamada de API (status code {response.status_code})."
    except requests.RequestException as e:
            return  f"Erro na chamada de API: {e}"
    
def put_respostas(payload):
    api_url = url + '/surprise-respostas'
    try:
        response = requests.request("POST", api_url, headers=headers, data=payload)
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            return f"Erro na chamada de API (status code {response.status_code})."
    except requests.RequestException as e:
            return  f"Erro na chamada de API: {e}"