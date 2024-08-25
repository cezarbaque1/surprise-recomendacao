import pandas as pd

def get_questions():
    # Dados fornecidos
    dados = {
        'idPergunta': [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5],
        'idResposta': ['1-1', '1-2', '1-3', '2-1', '2-2', '2-3', '3-1', '3-2', '3-3', '4-1', '4-2', '4-3', '4-4', '5-1', '5-2', '5-3'],
        'Pergunta': [
            'Qual seu Gênero', 'Qual seu Gênero', 'Qual seu Gênero',
            'Onde você prefere passar suas férias?', 'Onde você prefere passar suas férias?', 'Onde você prefere passar suas férias?',
            'O que você pensa sobre signos?', 'O que você pensa sobre signos?', 'O que você pensa sobre signos?',
            'Chegou o final de semana e você vai decidir o que fazer, o que vem primeiro na sua cabeça?', 'Chegou o final de semana e você vai decidir o que fazer, o que vem primeiro na sua cabeça?', 'Chegou o final de semana e você vai decidir o que fazer, o que vem primeiro na sua cabeça?', 'Chegou o final de semana e você vai decidir o que fazer, o que vem primeiro na sua cabeça?',
            'Você chegou em uma sala onde não conhece ninguém, o que você faz?', 'Você chegou em uma sala onde não conhece ninguém, o que você faz?', 'Você chegou em uma sala onde não conhece ninguém, o que você faz?'
        ],
        'Resposta': [
            'Masculino', 'Feminino', 'Outro',
            'Praia', 'Montanha', 'Tanto faz',
            'Já acertou muita coisa sobre mim', 'Fiz meu mapa astral uma vez', 'Não acredito que a posição dos planetas influenciem minha vida',
            'Cineminha top', 'Um Barzinho de leve', 'Ficar em casa', 'Balada pesaaaada',
            'Fico observando para ver se não conheço alguém', 'Vejo se tem alguém interessante para conhecer', 'Depende do meu humor, as vezes fico na minha e as vezes tento puxar assunto'
        ],
        'PerguntaOutro': [
            'Qual o Gênero dele(a)', 'Qual o Gênero dele(a)', 'Qual o Gênero dele(a)',
            'Onde ele(a) prefere passar suas férias?', 'Onde ele(a) prefere passar suas férias?', 'Onde ele(a) prefere passar suas férias?',
            'O que ele(a) pensa sobre signos?', 'O que ele(a) pensa sobre signos?', 'O que ele(a) pensa sobre signos?',
            'Chegou o final de semana e ele(a) vai decidir o que fazer, o que vem primeiro na sua cabeça?', 'Chegou o final de semana e ele(a) vai decidir o que fazer, o que vem primeiro na sua cabeça?', 'Chegou o final de semana e ele(a) vai decidir o que fazer, o que vem primeiro na sua cabeça?', 'Chegou o final de semana e ele(a) vai decidir o que fazer, o que vem primeiro na sua cabeça?',
            'Ele(a) chegou em uma sala onde não conhece ninguém, o que faz?', 'Ele(a) chegou em uma sala onde não conhece ninguém, o que faz?', 'Ele(a) chegou em uma sala onde não conhece ninguém, o que faz?'
        ],
        'RespostaOutro': [
            'Masculino', 'Feminino', 'Outro',
            'Praia', 'Montanha', 'Tanto faz',
            'Já acertou muita coisa sobre ele(a)', 'Fez meu mapa astral uma vez', 'Não acredita que a posição dos planetas influenciem a vida',
            'Cineminha top', 'Um Barzinho de leve', 'Ficar em casa', 'Balada pesaaaada',
            'Fica observando para ver se não conheçe alguém', 'Vê se tem alguém interessante para conhecer', 'Depende do humor, as vezes fica na dale(a) e as vezes tenta puxar assunto'
        ]
    }
    # Criação do DataFrame
    dfPerguntas = pd.DataFrame(dados)
    return dfPerguntas