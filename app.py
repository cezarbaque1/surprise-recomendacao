import streamlit as st
import json
from conn.perguntas import *
from conn.apis import *
from datetime import datetime
from conn.predict import predict

st.set_page_config(page_title="Surprise - Recomendação de Produtos", layout="centered", menu_items=None, initial_sidebar_state="collapsed")

st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)

st.markdown("""
    <style>
    .stButton button {
        float: left;
        position: relative;
        left: 25%;
        width: 50%;
    }
    </style>
""", unsafe_allow_html=True)


def caracteristicas():
    perguntas = get_questions()
    perguntas_base = perguntas.groupby(['idPergunta', 'Pergunta', 'PerguntaOutro']).agg(list).reset_index()

    st.title('Surprise!')
    st.subheader('Fale um pouco sobre o que o seu Presenteado gosta!')

    # Dicionário para armazenar as respostas
    responses = {}

    # Loop pelas perguntas e cria campos de entrada com opções
    for index, item in perguntas_base.iterrows():
        # print(item['idPergunta'])
        response = st.radio(item['PerguntaOutro'], item['RespostaOutro'])
        linhadf = perguntas[perguntas['RespostaOutro'] == response].reset_index()
        responses[item['idPergunta']] = linhadf.loc[0, 'Resposta']

    # Botão para salvar as respostas
    if st.button('Recomendar Produtos'):
        st.session_state.state = 'produtos'
        st.session_state.payload = responses
        st.rerun()
    

def select_product():
    st.title('Presentes para o seu Presenteado')
    products = st.session_state.products #caso a variavel for dataframe

    col1, col2, col3 = st.columns([1,3,1])
    col2.image(products.iloc[st.session_state.nproduct]['thumbnail'], caption=products.iloc[st.session_state.nproduct]['name'], use_column_width=True)

    col1, col2, col3 = st.columns(3)
    # if col2.button('Ver Loja'):
    #     st.session_state.state = 'thankyou'
    #     del st.session_state.products
    #     del st.session_state.nproduct
    #     st.rerun()
    
    if col1.button('Sair'):
        del st.session_state.state
        del st.session_state.nproduct
        st.rerun()
    
    st.markdown('<div class="right-align">', unsafe_allow_html=True)
    
    proximoEnabled = True if st.session_state.nproduct == 4 else False
    if col3.button('Outro', disabled=proximoEnabled):
        st.session_state.nproduct += 1
        
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

def thankyou():
    st.title('Obrigado por utilizar a Surprise')
    st.subheader('Volte sempre que quiser!')
    if st.button('Responder Novamente'):
        st.session_state.state = 'caracteristicas'
        st.rerun()

def mount_products():
    data = [json.loads(json.dumps(st.session_state.payload))]
    df = pd.DataFrame(data)
    prediction = predict(df)

    productsJson = get_all_products()
    products = pd.DataFrame(productsJson)
    products = products[products['idProduto'].isin(prediction)]
    st.session_state.products = products

#Define se vou mostrar as caracteristicas ou os produtos e pega os produtos se necessário
def main():
    if 'state' not in st.session_state:
        st.session_state.state = 'caracteristicas'
    
    if 'nproduct' not in st.session_state:
        st.session_state.nproduct = 0

    if st.session_state.state == 'produtos':
        if 'products' not in st.session_state:
            mount_products()
        select_product()
        
    
    if st.session_state.state == 'caracteristicas':
        caracteristicas()
    
    if st.session_state.state == 'thankyou':
        thankyou()

if __name__ == '__main__':
    main()