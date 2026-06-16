import os

import pandas as pd
import pytest

pytest.importorskip("sklearn")

MODELO = "modelo/predicao_surprise.pkl"


@pytest.mark.skipif(not os.path.exists(MODELO), reason="modelo não disponível")
def test_predict_retorna_top5():
    from conn.predict import predict

    df = pd.DataFrame(
        [
            {
                "1": "Masculino",
                "2": "Praia",
                "3": "Já acertou muita coisa sobre mim",
                "4": "Cineminha top",
                "5": "Fico observando para ver se não conheço alguém",
            }
        ]
    )
    result = predict(df)
    assert len(result) == 5
    assert len(set(result)) == 5  # sem duplicatas
