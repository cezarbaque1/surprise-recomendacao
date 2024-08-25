import streamlit as st
import json
from conn.perguntas import *
from conn.apis import *
from datetime import datetime
from st_clickable_images import clickable_images
from st_click_detector import click_detector

# st.set_page_config(page_title="Surprise - Recomendação de Produtos", layout="centered", menu_items=None)

def set_initial_variables():
    if "question" not in st.session_state:
        st.session_state["question"] = True

    if "selected" not in st.session_state:
        st.session_state["selected"] = -1

    if "clicked" not in st.session_state:
         st.session_state.clicked = ["", "", ""]
    else:
        for i, click in enumerate(st.session_state.clicked):
            if click != "":
                st.session_state.selected = i
            st.session_state.clicked = ["", "", ""]
    

def set_current_click(id):
    pass

def reset_checkbox(checkboxName):
    st.session_state[checkboxName] = not st.session_state.get(checkboxName, False)

def question1():

    st.write(st.session_state.clicked)
    opcoes = [{'url' : "<img src='https://img.freepik.com/vetores-gratis/praia-com-cena-de-paisagem-marinha-de-coquetel-de-coco_603843-2345.jpg' style='margin: 5px; height: 200px; opacity: 0.5;'>" , 'texto' : 'Praia'},
            {'url' : "<img src='https://img.freepik.com/vetores-gratis/plano-de-fundo-plano-de-aventura_23-2149037512.jpg' style='margin: 5px; height: 200px; opacity: 0.5;'>",'texto' : 'Montanha'},
            {'url' : "<img src='https://img.freepik.com/vetores-gratis/pessoas-planas-organicas-fazendo-perguntas_23-2148919414.jpg' style='margin: 5px; height: 200px; opacity: 0.5;'>", 'texto' : 'Tanto Faz'}]

    # opcoes = [{'url' : 'https://img.freepik.com/vetores-gratis/praia-com-cena-de-paisagem-marinha-de-coquetel-de-coco_603843-2345.jpg' , 'texto' : 'Praia'},
    #         {'url' : "<img src=https://img.freepik.com/vetores-gratis/plano-de-fundo-plano-de-aventura_23-2149037512.jpg",'texto' : 'Montanha'},
    #         {'url' : "https://img.freepik.com/vetores-gratis/pessoas-planas-organicas-fazendo-perguntas_23-2148919414.jpg", 'texto' : 'Tanto Faz'}]

    for i, opcao in enumerate(opcoes):
        st.session_state.clicked[i] = click_detector(f"<a href='#' id='{i}'>{opcao['url']}</a>", 
                                                     key='teste' + str(i))
        st.write(opcao['texto'])

    st.write(st.session_state.selected)

    # st.write('Posição Selecionada: ' + str(st.session_state.selected))

    # for i, opcao in enumerate(opcoes):
    #     st.session_state.clicked[i]  = clickable_images([opcao['url']], 
    #                             titles=[opcao['texto']], 
    #                             div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
    #                             img_style={"margin": "5px", "height": "200px", 'opacity' : '0.5'},
    #                             key='image' + str(i))
        
    #     st.markdown(f"Image #{st.session_state.clicked[i]} clicked" if st.session_state.clicked[i] > -1 else "No image clicked")
    
    # st.write(st.session_state.image0)
    # clicked  = clickable_images([opcoes[0]['url'], opcoes[1]['url'], opcoes[2]['url']], 
    #                          titles=[opcoes[0]['texto'], opcoes[1]['texto'], opcoes[2]['texto']], 
    #                          div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
    #                          img_style={"margin": "5px", "height": "200px", 'opacity' : '0.5'},)

    # st.write(st.session_state.clicked)



def main():
    st.title('Surprise!')
    set_initial_variables()
    question1()

if __name__ == '__main__':
    main()