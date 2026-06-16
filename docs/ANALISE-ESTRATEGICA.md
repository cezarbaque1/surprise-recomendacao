# Análise Estratégica — Surprise

> Registro de uma avaliação crítica de viabilidade de negócio (junho/2026).
> **Conclusão prática: o projeto foi descontinuado como produto/venture.** Este
> documento preserva o raciocínio que levou a essa decisão.

## A pergunta central

> Uma LLM básica (ChatGPT, Gemini etc.) não substituiria facilmente esta
> ferramenta? Como diferenciar?

## Resposta: sim — o núcleo do Surprise é commodity

O coração da ferramenta é "5 perguntas → modelo → 5 produtos de um catálogo
Nike/Polishop". Uma LLM gratuita faz isso **melhor** em quase tudo que importa
para a recomendação em si:

- **Personalização**: linguagem natural supera 5 perguntas fixas de personalidade.
- **Catálogo**: a web inteira vs. ~481 itens de dois lojistas.
- **Explicação**: a LLM justifica *por que* o presente combina; o Surprise só
  retorna um ID de produto.
- **Manutenção**: zero ML para retreinar.

Ou seja, **o algoritmo de recomendação não é diferencial — é commodity.**

## A única fresta real: a LLM recomenda, mas não transaciona

A diferenciação possível não está em "recomendar", e sim em **comprar de verdade**:

- A LLM **alucina** produto, preço e link; não sabe o que está **em estoque**
  agora, por R$X, com entrega para um CEP.
- Não tem **checkout, garantia de disponibilidade, troca, frete, nota fiscal**.
- Não resolve a **monetização/atribuição** disso (assistentes de IA estão,
  inclusive, quebrando a atribuição de afiliados).

Mas preencher essa fresta significa virar uma empresa de **integração de
comércio + logística** — concorrendo com Mercado Livre, Amazon e Google Shopping,
que já têm catálogo, estoque e operação. É jogo de operação, não de modelo.

## Reavaliação dos modelos de negócio

Pergunta de teste para cada um: **"o moat é o algoritmo?"**

| Modelo | Moat é a IA? | Veredito crítico |
|---|---|---|
| Afiliado B2C (atual) | Não | Commodity, margem baixa; assistentes de IA corroem a atribuição. Frágil. |
| White-label "gift finder" SaaS | **Não** | Pouco defensável: o cliente substitui por uma chamada de LLM. (Recuo de uma recomendação anterior que superestimava esse caminho.) |
| Lembretes / ocasião | Não | Retenção real, mas qualquer LLM + calendário faz. Feature, não negócio. |
| Corporate gifting | **Não** | É negócio de verdade, mas o moat é logística, fornecedores, budget e integração RH/CRM. A IA é a parte *menos* importante — seria outra empresa. |
| Wishlist / group gifting | Não, mas tem **efeito de rede** | Único moat estrutural (rede de listas que a LLM não replica). Mas é outro produto. |

## Veredito honesto

Como **app B2C autônomo de "quiz que recomenda presente", o Surprise não tem
moat durável** e a substituição por LLM é credível. O fato de **Etsy (Gift Mode),
Target (Gift Finder) e Amazon (Rufus)** já entregarem isso embutido e de graça é
evidência *contra* uma startup standalone, não a favor.

O valor real está em coisas que **não são o recomendador**:

1. **Integração de comércio + acionabilidade** (estoque/preço/entrega reais) —
   mas concorrendo com marketplaces.
2. **Distribuição** (estar no ponto da decisão de compra) — o ativo é o
   canal/audiência, não o modelo.
3. **Efeito de rede** (listas / group gifting).
4. **Curadoria com taste/marca** em nicho (ex.: só artesanal local, só
   sustentável) — margem de mídia, não de tecnologia.

## Decisão

O Surprise **não segue como venture**. Seu melhor destino é:

- **Projeto de portfólio**: demonstra o ciclo completo — dados → modelo →
  produto → deploy (Streamlit + API serverless + afiliados).
- Ou, eventualmente, uma **feature dentro de um varejista** que já tenha
  catálogo e logística.

As melhorias técnicas implementadas (segurança, correção de data leakage,
testes, CI, UX) seguem válidas como aprendizado e como portfólio, mesmo com o
produto descontinuado.

## Fontes do benchmark

- Smart Gift AI — Best AI Gift Finders 2025: https://smartgiftai.com/best-ai-gift-finders-2025/
- Etsy Gift Mode (TechCrunch): https://techcrunch.com/2024/01/24/etsy-launches-gift-mode-a-new-ai-powered-feature-that-generates-200-gift-guides
- Target AI Gift Finder (Retail Dive): https://www.retaildive.com/news/target-ai-gift-finder-online-shopping-assistant/735080/
- PerkUp — Top Corporate Gifting Platforms 2025: https://perkupapp.com/post/top-corporate-gifting-platforms-of-2025
- Snappy Gifts (Wikipedia): https://en.wikipedia.org/wiki/Snappy_Gifts
