import streamlit as st
import json
from conn.perguntas import *
from conn.apis import *
from datetime import datetime

def caracteristicas():
    perguntas = get_questions()
    perguntas_base = perguntas.groupby(['idPergunta', 'Pergunta']).agg(list).reset_index()

    st.title('Perguntas sobre Você')

    # Dicionário para armazenar as respostas
    responses = {}

    # Loop pelas perguntas e cria campos de entrada com opções
    for index, item in perguntas_base.iterrows():
        # print(item['idPergunta'])
        response = st.radio(item['Pergunta'], item['Resposta'])
        responses[item['idPergunta']] = response

    # Botão para salvar as respostas
    if st.button('Próximo'):
        st.session_state.state = 'produtos'
        st.session_state.payload = responses
        st.rerun()

#Define se vou mostrar as caracteristicas ou os produtos
def select_product():
    st.title('Qual produto você gosta?')
    products = st.session_state.products #caso a variavel for dataframe
    col1, col2 = st.columns(2)
    productReponses = [None,None,None,None,None,None]
    respostas = ['Não Gostei', 'Mais ou Menos', 'Amei!']

    for index, item in products.iloc[0:3].iterrows():
        col1.image(item['thumbnail'], caption=item['name'])
        reponseProd = col1.radio('O que achou?', respostas, key=index)
        productReponses[index] = {'produto' : item['idProduto'], 'response' : reponseProd }

    for index, item in products.iloc[3:7].iterrows():
        col2.image(item['thumbnail'], caption=item['name'])
        reponseProd = col2.radio('O que achou?', respostas , key=index)
        productReponses[index] = {'produto' : item['idProduto'], 'response' : reponseProd }
    
    responses = st.session_state.payload
    responses['produtos'] = productReponses

    if st.button('Finalizar'):

        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        responses['idResposta'] = timestamp

        payload = json.dumps(responses)
        retorno = put_respostas(payload)
        if retorno == []:
            st.markdown(retorno)
            st.json(responses)
            st.session_state.state = 'caracteristicas'
            del st.session_state.products
            st.rerun()
        else:
            st.error(retorno)



#Define se vou mostrar as caracteristicas ou os produtos e pega os produtos se necessário
def main():
    if 'state' not in st.session_state:
        st.session_state.state = 'caracteristicas'
    
    if st.session_state.state == 'produtos':
        if 'products' not in st.session_state:
            products = get_all_products()
            products = pd.DataFrame(products)
            products = products.sample(n=6).reset_index()
            st.session_state.products = products
            
        select_product()
    else:
        caracteristicas()

if __name__ == '__main__':
    main()