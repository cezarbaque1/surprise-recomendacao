import streamlit as st
import json
import os
from conn.perguntas import *
from conn.apis import *
from datetime import datetime

def main():
    perguntas = get_questions()
    perguntas_base = perguntas.groupby(['idPergunta', 'Pergunta']).agg(list).reset_index()

    st.title('Treinamento do Algoritmo')

    # Dicionário para armazenar as respostas
    responses = {}

    # Loop pelas perguntas e cria campos de entrada com opções
    for index, item in perguntas_base.iterrows():
        # print(item['idPergunta'])
        response = st.radio(item['Pergunta'], item['Resposta'])
        responses[item['idPergunta']] = response

    # Botão para salvar as respostas
    if st.button('Salvar Respostas'):
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        responses['idResposta'] = timestamp
        st.json(responses)
        payload = json.dumps(responses)
        retorno = put_respostas(payload)
        if retorno == []:
            st.success(f'Resposta salva com sucesso')
        else:
            st.error(retorno)


if __name__ == '__main__':
    main()