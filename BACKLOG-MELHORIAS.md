# 🗂️ Backlog de Melhorias — Surprise

Mapeamento de pontos de melhoria da aplicação em todos os âmbitos, priorizados por
**impacto × esforço**. Marque os itens conforme forem concluídos.

Legenda de prioridade: 🔴 Alta · 🟡 Média · 🟢 Baixa
Esforço estimado: P (pequeno) · M (médio) · G (grande)

---

## ✅ Progresso (entregue na branch `melhorias/surprise`)

- **Sprint 1 — Segurança e base:** S2, S3, S4, Q1, Q2, Q4 + README/D1.
- **Sprint 2 — Modelo:** M1 (data leakage), M2 (BernoulliNB), M3 (validação cruzada), D4 (pytest).
- **Sprint 3 — Produto:** U1 (link de compra), U2 (preço), U3 (spinner), S5 (página de treino protegida).
- **Sprint 4 — Arquitetura/DevOps:** A2 (config central), A3 (docs/API.md), A4 (mover artefatos), Q3 (sandbox/), Q8 (ruff), D2 (LICENSE), D3 (CI), S1 (mitigação documentada).

**Pendentes para próximas rodadas:** S6, Q5, Q6, Q7, M4, M5, M6 (LFS — exige reescrita de histórico), U4, U5, A1, D5.

---

## 🔒 Segurança

| # | Prioridade | Esforço | Item |
|---|-----------|---------|------|
| S1 | 🔴 | M | **RCE via pickle remoto.** `naive_test.ipynb`/`naive_training.ipynb` baixam o modelo da API e fazem `joblib.load` de conteúdo remoto. Desserializar pickle de fonte não confiável permite execução de código arbitrário. Validar origem/integridade (hash assinado) ou trocar o formato de serialização. |
| S2 | 🔴 | P | **Autenticação fraca.** O header `x-token` usa um valor placeholder (`'123'`). Definir tokens reais, rotacionáveis, e tratar a API como pública/sensível. |
| S3 | 🔴 | P | **Crash quando não há credenciais.** Em `conn/apis.py`, se `var.token` não existir e não houver env vars, `token` fica indefinido e `headers = {'x-token': token}` quebra com `NameError`. Adicionar valores padrão e mensagem de erro clara. |
| S4 | 🟡 | P | **Gestão de segredos.** Criar `.env.example` e documentar; padronizar para `python-dotenv` em vez de `var/token.py`. |
| S5 | 🟡 | P | **Página de treino exposta.** `pages/treinamento.py` é acessível por qualquer visitante e grava dados na base. Proteger com autenticação simples ou feature flag. |
| S6 | 🟢 | P | **Sem validação de entrada** nas respostas enviadas à API. |

---

## 🧹 Qualidade de Código

| # | Prioridade | Esforço | Item |
|---|-----------|---------|------|
| Q1 | 🟡 | P | **Imports curinga frágeis.** `from conn.perguntas import *` e `from conn.apis import *`. O `pd` usado em `app.py` só existe por importação transitiva. Importar explicitamente o que se usa. |
| Q2 | 🟡 | P | **API deprecada do Streamlit.** `use_column_width` foi substituído por `use_container_width`. |
| Q3 | 🟡 | M | **Arquivos exploratórios versionados.** `app_test.py`, `teste.py` e `naive_test.ipynb` contêm código comentado/experimental. Remover ou mover para uma pasta `sandbox/`. |
| Q4 | 🟡 | P | **`requirements.txt` incompleto e sem versões.** Faltam `joblib`, `python-dotenv` (se adotado), `openpyxl`. Fixar versões (pinning). |
| Q5 | 🟢 | P | **Tratamento de erro inconsistente.** `make_request` retorna string de erro ou dados; chamadores comparam `retorno == []`. Padronizar (exceções ou retorno estruturado). |
| Q6 | 🟢 | P | **Perguntas duplicadas** em `conn/perguntas.py` e `base_perguntas.ipynb`. Centralizar numa única fonte. |
| Q7 | 🟢 | P | **Typos e mistura PT/EN** em variáveis e textos de UI (ex.: "conheçe", "dale(a)"). |
| Q8 | 🟢 | P | **Linter/formatter.** Adicionar `ruff`/`black` + config. |

---

## 🤖 Modelo / Data Science

| # | Prioridade | Esforço | Item |
|---|-----------|---------|------|
| M1 | 🔴 | M | **Vazamento de dados (data leakage).** Em `naive_training.ipynb`, as linhas "Amei" são duplicadas **antes** do `train_test_split`, então a mesma observação pode cair em treino e teste, inflando a acurácia. Fazer o split antes de qualquer aumento de dados. |
| M2 | 🟡 | P | **Algoritmo inadequado.** `GaussianNB` assume features contínuas, mas a entrada é one-hot (binária). Usar `BernoulliNB` ou `CategoricalNB`. |
| M3 | 🟡 | M | **Avaliação fraca.** Só uma acurácia, sem validação cruzada, baseline ou tratamento de desbalanceamento. Adicionar métricas (precision@k, recall) e cross-validation. |
| M4 | 🟡 | G | **Personalização limitada.** A recomendação usa apenas 5 perguntas genéricas, ignorando atributos dos produtos. Explorar features de produto / filtragem colaborativa real. |
| M5 | 🟢 | P | **Versionamento de modelo.** Há `predicao_surprise.pkl` e `predicao_surprise2.pkl` sem critério claro. Definir convenção de versão e registrar metadados. |
| M6 | 🟢 | M | **Binários no git.** `.pkl`, `.docx`, `.xlsx` versionados incham o repositório. Usar Git LFS ou armazenamento externo. |

---

## 🎨 UX / Produto

| # | Prioridade | Esforço | Item |
|---|-----------|---------|------|
| U1 | 🔴 | P | **Sem link de compra (monetização quebrada).** O botão "Ver Loja" está comentado em `app.py`; os produtos recomendados não levam ao link de afiliado, embora o dado exista. Reativar e exibir o link. |
| U2 | 🟡 | P | **Cards pobres.** Só imagem + nome. Exibir preço, descrição e parcelamento (já vêm nos feeds). |
| U3 | 🟡 | M | **Feedback e estados de carregamento.** Adicionar spinners e mensagens ao consultar a API. |
| U4 | 🟢 | M | **Acessibilidade e responsividade** (mobile, contraste, alt text). |
| U5 | 🟢 | P | **Tela de "Obrigado"/saída** com call-to-action de recomeçar mais clara. |

---

## 🏛️ Arquitetura

| # | Prioridade | Esforço | Item |
|---|-----------|---------|------|
| A1 | 🟡 | G | **Dependência total da API externa.** Não há modo local/mock; impossível rodar offline. Criar camada de mock/fixtures para desenvolvimento e testes. |
| A2 | 🟡 | M | **Configuração dispersa.** Dois caminhos (env vs `var/token.py`) sem config central. Criar módulo `config.py` único. |
| A3 | 🟢 | M | **Back-end fora do repo e sem documentação.** Documentar contrato das rotas (`surprise-produtos`, `surprise-respostas`, `surprise-predict`). |
| A4 | 🟢 | P | **Artefatos no lugar errado.** Relatórios `.docx`/`.xlsx` dentro de `images/`. Mover para `docs/`. |

---

## ⚙️ DevOps / Infra

| # | Prioridade | Esforço | Item |
|---|-----------|---------|------|
| D1 | 🔴 | P | ✅ **README** — criado nesta rodada. |
| D2 | 🟡 | P | **LICENSE** ausente. Definir licença do projeto. |
| D3 | 🟡 | M | **CI/CD.** Pipeline com lint + testes (GitHub Actions). |
| D4 | 🟡 | M | **Testes automatizados.** Não há testes reais (os arquivos `*_test` são exploratórios). Adicionar `pytest` para `predict`, `perguntas` e `apis` (com mock). |
| D5 | 🟢 | P | **Deploy documentado.** Instruções de publicação (Streamlit Community Cloud / container). |

---

## 🎯 Sugestão de ordem de execução (sprints)

1. **Sprint 1 — Fundações & segurança rápida:** D1 ✅, S2, S3, S4, Q1, Q2, Q4.
2. **Sprint 2 — Confiabilidade do modelo:** M1, M2, M3, D4.
3. **Sprint 3 — Produto & monetização:** U1, U2, U3, S5.
4. **Sprint 4 — Arquitetura & DevOps:** A1, A2, D3, M6, S1.
