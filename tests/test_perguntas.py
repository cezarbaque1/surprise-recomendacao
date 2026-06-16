from conn.perguntas import get_questions


def test_get_questions_estrutura():
    df = get_questions()
    assert list(df.columns) == [
        "idPergunta",
        "idResposta",
        "Pergunta",
        "Resposta",
        "PerguntaOutro",
        "RespostaOutro",
    ]
    # 5 perguntas, 15 respostas no total
    assert len(df) == 15
    assert df["idPergunta"].nunique() == 5


def test_get_questions_sem_nulos():
    df = get_questions()
    assert not df.isnull().values.any()
