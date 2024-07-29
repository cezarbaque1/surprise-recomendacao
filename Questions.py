import streamlit as st
import json
import os
from datetime import datetime

# Função para salvar dados em um arquivo JSON
def save_data(data, filename='data.json', folder='responses'):
    if not os.path.exists(folder):
        os.makedirs(folder)
    filepath = os.path.join(folder, filename)
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)

# Perguntas padrão com opções
questions_with_options = {
    "Qual seu Gênero?": ["Masculino", "Feminino", "Outro"],
    "Onde você prefere passar suas férias?": ["Campo", "Praia","Cidade","Tanto faz"],
    "O que você pensa sobre signos?": ["Já acertou muita coisa sobre mim", "Fiz meu mapa astral uma vez", "Não acredito que a posição dos planetas influencie minha vida"],
    "Chegou o final de semana e você vai decidir o que fazer, o que vem primeiro na sua cabeça?": ["Cineminha top", "Balada pesaaaada", "Viajar para algum lugar", "Descansar em casa", "Praticar esportes"],
    "Você chegou em uma sala onde não conhece ninguém, o que você faz?": ["Fico observando para ver se não conheço alguém", "Vejo se tem alguém interessante para conhecer", "Depende do meu humor, as vezes fico na minha e as vezes tento puxar assunto"],
}

st.title('Formulário de Perguntas')

# Dicionário para armazenar as respostas
responses = {}

# Loop pelas perguntas e cria campos de entrada com opções
for question, options in questions_with_options.items():
    response = st.radio(question, options)
    responses[question] = response

# Botão para salvar as respostas
if st.button('Salvar Respostas'):
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    filename = f'responses_{timestamp}.json'
    save_data(responses, filename)
    st.success(f'Respostas salvas em {filename}')
