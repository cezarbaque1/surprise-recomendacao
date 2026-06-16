import json

import pandas as pd
import streamlit as st

from conn.apis import get_all_products
from conn.perguntas import get_questions
from conn.predict import predict

st.set_page_config(page_title="Surprise - Recomendação de Produtos", layout="centered", menu_items=None, initial_sidebar_state="collapsed")

# Esconde o controle de expandir a sidebar (navegação interna de páginas)
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


def _reset():
    """Limpa o estado da sessão para recomeçar o fluxo."""
    for chave in ('state', 'nproduct', 'products', 'payload'):
        st.session_state.pop(chave, None)


def caracteristicas():
    perguntas = get_questions()
    perguntas_base = perguntas.groupby(['idPergunta', 'Pergunta', 'PerguntaOutro']).agg(list).reset_index()

    st.title('🎁 Surprise!')
    st.subheader('Fale um pouco sobre o que o seu Presenteado gosta!')
    st.caption('Responda 5 perguntas rápidas e a gente sugere o presente ideal.')

    # Dicionário para armazenar as respostas
    responses = {}

    # Loop pelas perguntas e cria campos de entrada com opções
    for _, item in perguntas_base.iterrows():
        st.divider()
        opcoes = item['RespostaOutro']
        # Opções curtas ficam na horizontal (mais visual); as longas, na vertical.
        horizontal = all(len(str(o)) <= 16 for o in opcoes)
        response = st.radio(item['PerguntaOutro'], opcoes, horizontal=horizontal)
        linhadf = perguntas[perguntas['RespostaOutro'] == response].reset_index()
        responses[item['idPergunta']] = linhadf.loc[0, 'Resposta']

    st.divider()
    if st.button('🔮 Recomendar Produtos', type='primary', use_container_width=True):
        st.session_state.state = 'produtos'
        st.session_state.payload = responses
        st.session_state.nproduct = 0
        st.rerun()


def _formata_preco(valor):
    """Formata o preço no padrão R$ 0,00; devolve None se inválido."""
    if valor in (None, '', 'null'):
        return None
    try:
        return f"R$ {float(valor):.2f}".replace('.', ',')
    except (TypeError, ValueError):
        return None


def _parcelamento(valor, n=10):
    """Texto de parcelamento simples a partir do preço (ex.: 'em até 10x de R$ ...')."""
    try:
        parcela = float(valor) / n
    except (TypeError, ValueError):
        return None
    if parcela <= 0:
        return None
    return f"ou em até {n}x de R$ {parcela:.2f}".replace('.', ',')


def select_product():
    products = st.session_state.products
    total = len(products)
    idx = st.session_state.nproduct
    produto = products.iloc[idx]

    st.title('Presentes para o seu Presenteado')
    st.caption(f'Sugestão {idx + 1} de {total}')
    st.progress((idx + 1) / total)

    # Card do produto
    with st.container(border=True):
        col1, col2, col3 = st.columns([1, 6, 1])
        col2.image(produto['thumbnail'], caption=produto['name'], use_column_width=True)
        preco = _formata_preco(produto.get('price'))
        if preco:
            col2.subheader(preco)
        parcela = _parcelamento(produto.get('price'))
        if parcela:
            col2.caption(parcela)

    # CTA principal (monetização) — link de afiliado em destaque
    link = produto.get('link')
    if link:
        st.link_button('🛒 Ver na Loja', link, type='primary', use_container_width=True)

    # Navegação entre as sugestões
    nav_anterior, nav_proximo = st.columns(2)
    if nav_anterior.button('◀ Anterior', disabled=(idx == 0), use_container_width=True):
        st.session_state.nproduct -= 1
        st.rerun()
    if nav_proximo.button('Próximo ▶', disabled=(idx >= total - 1), use_container_width=True):
        st.session_state.nproduct += 1
        st.rerun()

    if idx >= total - 1:
        st.success('Essas foram nossas sugestões! 🎁')

    st.divider()
    if st.button('↺ Recomeçar', use_container_width=True):
        _reset()
        st.rerun()


def thankyou():
    st.title('Obrigado por utilizar a Surprise')
    st.subheader('Volte sempre que quiser!')
    if st.button('Responder Novamente'):
        _reset()
        st.rerun()


def _filtra_por_genero(products, genero):
    """Remove produtos do gênero oposto ao informado (heurística pelo nome).

    Mantém unissex/infantil. Se o filtro zerar a lista, devolve a original.
    """
    if genero not in ('Masculino', 'Feminino') or products.empty:
        return products
    nome = products['name'].str.lower()
    incompativel = nome.str.contains('femin') if genero == 'Masculino' else nome.str.contains('mascul')
    filtrado = products[~incompativel]
    return filtrado if not filtrado.empty else products


def mount_products():
    data = [json.loads(json.dumps(st.session_state.payload))]
    df = pd.DataFrame(data)
    prediction = predict(df)

    productsJson = get_all_products()
    products = pd.DataFrame(productsJson)
    products = products[products['idProduto'].isin(prediction)]

    # Filtra por gênero informado na 1ª pergunta para aumentar a relevância
    genero = st.session_state.payload.get(1)
    products = _filtra_por_genero(products, genero).reset_index(drop=True)

    st.session_state.products = products
    st.session_state.nproduct = 0

#Define se vou mostrar as caracteristicas ou os produtos e pega os produtos se necessário
def main():
    if 'state' not in st.session_state:
        st.session_state.state = 'caracteristicas'

    if 'nproduct' not in st.session_state:
        st.session_state.nproduct = 0

    if st.session_state.state == 'produtos':
        if 'products' not in st.session_state:
            with st.spinner('Buscando as melhores recomendações...'):
                mount_products()
        select_product()

    if st.session_state.state == 'caracteristicas':
        caracteristicas()

    if st.session_state.state == 'thankyou':
        thankyou()

if __name__ == '__main__':
    main()
