# Contrato da API — Surprise

Back-end serverless (AWS API Gateway, região `us-east-2`). O código do back-end
**não** faz parte deste repositório. Todas as chamadas exigem o header de
autenticação `x-token`.

Base URL e token são configurados via `URL`/`TOKEN` (env, `.env` ou `var/token.py`).

## Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| `GET`  | `/surprise-produtos?idProduto=all` | Lista todos os produtos cadastrados |
| `POST` | `/surprise-produtos` | Cadastra/atualiza produtos (JSON em formato `records`) |
| `GET`  | `/surprise-respostas?idResposta=all` | Lista todas as respostas coletadas |
| `POST` | `/surprise-respostas` | Salva uma resposta de questionário + avaliações |
| `POST` | `/surprise-predict` | Publica o modelo treinado (`{"file": "<base64>"}`) |
| `GET`  | `/surprise-predict` | Baixa o modelo publicado (base64) |

## Formato dos dados

### Produto
```json
{
  "idProduto": "DN4181010",
  "name": "Plus Size - Top Nike Dri-FIT Indy Feminino",
  "price": "161.49",
  "link": "https://redir.lomadee.com/...",
  "thumbnail": "https://imgnike-a.akamaihd.net/...",
  "loja": "ofertas-nike",
  "firstName": "Plus"
}
```

### Resposta (questionário + avaliações)
```json
{
  "1": "Feminino",
  "2": "Montanha",
  "3": "Já acertou muita coisa sobre mim",
  "4": "Um Barzinho de leve",
  "5": "Depende do meu humor...",
  "produtos": [{"produto": "CJ2297063", "response": "Mais ou Menos"}],
  "idResposta": "20240731210509"
}
```

> ⚠️ **Segurança (S1):** o endpoint `/surprise-predict` trafega o modelo como
> pickle em base64. Fazer `joblib.load` de um pickle vindo da rede permite
> **execução de código arbitrário** se a fonte for comprometida. Carregue apenas
> modelos de origem confiável e, idealmente, valide a integridade (hash assinado)
> antes de desserializar.
