# 🎁 Surprise — Recomendação de Presentes

Aplicação web que **recomenda presentes** com base no perfil de quem vai ser presenteado.
O usuário responde a 5 perguntas rápidas sobre a personalidade e os gostos do "presenteado"
e um modelo de Machine Learning sugere os produtos com maior chance de agradar.

> Projeto Aplicado de Pós-Graduação. Front-end em [Streamlit](https://streamlit.io/),
> modelo em scikit-learn e back-end serverless na AWS (API Gateway + Lambda).

---

## ✨ O que a aplicação faz

### 1. Fluxo de recomendação (`app.py`)
1. O usuário responde 5 perguntas sobre o presenteado:
   - Gênero
   - Onde prefere passar as férias (praia / montanha / tanto faz)
   - O que pensa sobre signos
   - O que faz no fim de semana
   - Como age numa sala cheia de desconhecidos
2. As respostas são enviadas ao modelo treinado (`modelo/predicao_surprise.pkl`).
3. O modelo retorna os **5 produtos mais prováveis** de agradar.
4. Os produtos (imagem + nome) são exibidos um a um, com botões **Outro** (próximo) e **Sair**.

### 2. Fluxo de coleta/treino (`pages/treinamento.py`)
Página usada para **gerar dados de treino**. Mostra 6 produtos aleatórios; o usuário avalia
cada um (*Não Gostei* / *Mais ou Menos* / *Amei!*). As avaliações, junto com as respostas das
perguntas, são enviadas à API e passam a alimentar o modelo.

### 3. Pipeline de dados e modelo (notebooks)
- **`base_produtos.ipynb`** — lê os feeds de ofertas em `ofertas/*.xml` (Nike, Polishop via
  links de afiliado Lomadee), normaliza e cadastra os produtos na API.
- **`naive_training.ipynb`** — baixa as respostas coletadas, monta o dataset, treina um
  classificador **Gaussian Naive Bayes** (pipeline `OneHotEncoder` → `GaussianNB`), avalia,
  salva o `.pkl` e o publica na API em base64.
- **`naive_test.ipynb`** — baixa o modelo publicado e testa uma predição isolada.
- **`base_perguntas.ipynb`** — versão em notebook do banco de perguntas.

---

## 🏗️ Arquitetura

```
┌──────────────────────┐      x-token        ┌─────────────────────────┐
│   Streamlit (front)  │ ──────────────────► │   AWS API Gateway        │
│   app.py             │  surprise-produtos  │   /dev                   │
│   pages/treinamento  │  surprise-respostas │   (Lambda + storage)     │
└──────────┬───────────┘  surprise-predict   └─────────────────────────┘
           │
           ▼
   modelo/predicao_surprise.pkl  (GaussianNB + OneHotEncoder)
```

- **Front-end:** Streamlit (`app.py` + página `pages/treinamento.py`).
- **Camada de acesso:** `conn/apis.py` (HTTP), `conn/perguntas.py` (banco de perguntas),
  `conn/predict.py` (carrega o `.pkl` e prediz).
- **Back-end:** API Gateway na AWS (`us-east-2`), autenticado por header `x-token`. O código
  do back-end **não** faz parte deste repositório.
- **Modelo:** scikit-learn, serializado com `joblib`.

---

## 📁 Estrutura do projeto

```
surprise-recomendacao/
├── app.py                  # App principal — fluxo de recomendação
├── pages/treinamento.py    # Página de coleta de avaliações (treino)
├── conn/
│   ├── apis.py             # Chamadas HTTP à API (produtos/respostas/predict)
│   ├── perguntas.py        # Banco de perguntas (hardcoded)
│   └── predict.py          # Carrega o .pkl e gera a recomendação
├── modelo/                 # Modelos treinados (.pkl)
├── ofertas/                # Feeds XML de produtos (Nike, Polishop)
├── images/                 # Imagens e relatórios do projeto
├── base_produtos.ipynb     # ETL dos feeds → API
├── naive_training.ipynb    # Treino do modelo
├── naive_test.ipynb        # Teste do modelo
├── .streamlit/config.toml  # Tema/config do Streamlit
└── requirements.txt        # Dependências
```

---

## 🚀 Como executar localmente

> Requer Python 3.12.

```bash
# 1. Crie e ative um ambiente virtual
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux/Mac

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Configure as credenciais da API
#    Opção A — variáveis de ambiente:
set URL=https://<sua-api>/dev/
set TOKEN=<seu-token>
#    Opção B — crie var/token.py (ignorado pelo git) com:
#        url = "https://<sua-api>/dev/"
#        token = "<seu-token>"

# 4. Rode o app
streamlit run app.py
```

A aplicação depende da API externa para listar produtos e gerar recomendações; sem ela,
apenas a tela de perguntas é renderizada.

---

## 🔧 Configuração

| Variável | Onde | Descrição |
|----------|------|-----------|
| `URL`    | env ou `var/token.py` | Base URL da API Gateway |
| `TOKEN`  | env ou `var/token.py` | Token enviado no header `x-token` |

O arquivo `var/token.py` está no `.gitignore` e **não** deve ser versionado.

---

## 🛠️ Stack

- **Python 3.12**
- **Streamlit** — interface web
- **scikit-learn** — Gaussian Naive Bayes + OneHotEncoder
- **pandas / numpy** — manipulação de dados
- **lxml** — leitura dos feeds XML
- **requests** — integração com a API
- **joblib** — serialização do modelo

---

## 📌 Status e próximos passos

Há um backlog de melhorias mapeado em [`BACKLOG-MELHORIAS.md`](BACKLOG-MELHORIAS.md),
cobrindo segurança, qualidade de código, modelo de ML, UX, arquitetura e DevOps.
