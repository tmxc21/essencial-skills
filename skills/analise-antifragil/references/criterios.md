# Os 34 critérios — detalhamento e pontuação

Especificação de scoring do modelo v8. Cada critério tem uma nota de 0 até seu máximo. A soma dos critérios de uma camada é o **score bruto** da camada; esse bruto é normalizado (regra de três) e ponderado pelo peso da camada. A soma ponderada das 5 camadas = **score final 0–100**.

Legenda de procedência:
- `[rec]` = recuperado verbatim do painel v8 (valor confirmado)
- `[def]` = definido para completar o modelo autônomo — **conferir contra o doc-mestre** se houver divergência

Regra de dado ausente: sem dado confiável → nota conservadora (baixa), nunca estimativa apresentada como fato. Buscar na web quando verificável (fretes, CAPE, VIX, put/call, DXY, juros reais).

---

## Camada 1 — Macro & Ciclo · peso 20% · bruto 45

### (a) Indicadores financeiros
| # | Critério | Métrica | Máx |
|---|---|---|---|
| 1 | Fase do ciclo econômico | Posição no ciclo austríaco de crédito | 5 `[rec]` |
| 2 | Condição de liquidez global | Expansão/contração de liquidez | 5 `[rec]` |
| 3 | Força do dólar (DXY) | Nível e tendência do DXY | 5 `[rec]` |
| 4 | Ambiente de juros reais | Fed funds vs CPI em tempo real | 5 `[rec]` |
| 5 | Sustentabilidade fiscal EUA | Dívida/PIB + déficit primário | 5 `[rec]` |

### (b) Economia real
| # | Critério | Métrica | Máx |
|---|---|---|---|
| 6 | BDI — Baltic Dry Index | Frete de commodities secas — cai antes de recessões | 5 `[rec]` |
| 7 | SCFI — Shanghai Containerized Freight | Frete de manufaturados — ciclo de estoques global | 5 `[rec]` |
| 8 | WCI — World Container Index | Rotas globais, atualização semanal — termômetro mais rápido | 5 `[rec]` |
| 9 | PIB global vs volume de comércio | Comércio > PIB = globalização · invertido = desglobalização | 5 `[rec]` |

---

## Camada 2 — Fundamentos · peso 27% · bruto 30

| # | Critério | Métrica | Alerta | Máx |
|---|---|---|---|---|
| 10 | Free cash flow | FCF positivo e crescente 3+ trimestres | FCF neg./decrescente 3+ tri | 6 `[rec]` |
| 11 | Estrutura de custos | Margem operacional vs setor | Margem comprime com receita subindo | 6 `[rec]` |
| 12 | Endividamento | Dívida líq / EBITDA < 3x | Acima de 3x em setor não regulado | 6 `[rec]` |
| 13 | Inovação / moat | R&D % receita + vantagem competitiva | R&D caindo vs concorrência | 6 `[rec]` |
| 14 | Potencial setorial | TAM + crescimento projetado 5 anos | Setor maduro sem catalisador | 6 `[rec]` |

---

## Camada 3 — Valuation & Margem de Segurança · peso 21% · bruto 30

| # | Critério | Métrica | Máx |
|---|---|---|---|
| 15 | Múltiplo vs histórico | P/E, EV/EBITDA vs média 10 anos | 5 `[rec]` |
| 16 | CAPE / valuation absoluto | Shiller P/E do setor | 5 `[rec]` |
| 17 | Margem de segurança | Desconto vs valor intrínseco | 5 `[rec]` |
| 18 | Assimetria risco/retorno | Upside/downside ≥ 3x (lógica Kelly) | 5 `[rec]` |
| 19 | Janela de entrada | Preço vs média móvel 200d | 5 `[rec]` |
| 20 | Posicionamento ATH/ATL | Distância % do topo e do fundo históricos | 5 `[def]` |

---

## Camada 4 — Sentimento & Ciclo de Bolha · peso 17% · bruto 40

Base: tese do mentor — último otimista capitulando = fundo próximo (smart money já compra); mídia não especializada cobrindo = topo. Sentimento é **específico por ativo e por ciclo**, nunca universal.

| # | Critério | Métrica | Máx |
|---|---|---|---|
| 21 | Cobertura de mídia não especializada | Google Trends + veículos pop (CNN, Globo, TikTok fin.) | 5 `[rec]` |
| 22 | Volatilidade implícita (VIX) | VIX comprimido = euforia; explodindo = capitulação | 5 `[rec]` |
| 23 | Put/Call ratio | Abaixo de 0.7 = otimismo excessivo | 5 `[rec]` |
| 24 | Insider buying / smart money | Compras de insiders + fluxo institucional | 5 `[rec]` |
| 25 | X/Twitter — narrativa geral | Qual história domina sobre o ativo | 5 `[def]` |
| 26 | X/Twitter — velocidade de propagação | Aceleração da narrativa = proximidade de extremo | 5 `[def]` |
| 27 | X/Twitter — haters estruturais | Céticos persistentes como indicador contrário | 5 `[def]` |
| 28 | Ciclo histórico de sentimento do ativo | Onde o ativo está no próprio ciclo emocional histórico | 5 `[def]` |

---

## Camada 5 — Cisne Negro & Convexidade · peso 15% · bruto 30

Duas dimensões **separadas** (sensibilidade do ativo × exposição do portfólio) + natureza convexa/côncava + hedge de cauda.

| # | Critério | Métrica | Máx |
|---|---|---|---|
| 29 | Sensibilidade de preço a choque | Quanto o preço do ativo sofre num choque de cauda | 5 `[rec-conceito]` |
| 30 | Exposição do portfólio ao choque | Quanto o portfólio total sofre se o choque ocorrer | 5 `[rec-conceito]` |
| 31 | Convexidade vs concavidade | Ativo ganha com desordem (convexo) ou quebra (côncavo)? | 10 `[def]` |
| 32 | Fragilidade a evento-tese | Existe um único evento que invalida a tese inteira? | 5 `[def]` |
| 33 | Opcionalidade / hedge de cauda | Presença de upside assimétrico ou proteção de cauda | 5 `[def]` |

> Observação: os critérios 29–30 têm conceito recuperado (as duas dimensões do cisne negro) mas o split de pontos é reconstruído. Os critérios 31–33 completam a camada para fechar os 34 e devem ser conferidos contra o doc-mestre.

---

## Filtro Barsi (standalone — fora dos 34)

Qualificador **binário** de perenidade: o setor tem demanda inelástica que resiste a crise sem destruição de receita? (farmacêutico, energia elétrica, saneamento, bélico, alimentos básicos). Não altera nota — entra como flag **"Perene / Não perene"** no output. É o que qualifica um ativo para o bloco de 30% "Perenes" do barbell.

---

## Contagem

Macro 9 + Fundamentos 5 + Valuation 6 + Sentimento 8 + Cisne Negro 5 = **33 critérios mapeados**. O doc-mestre marca 34 — há 1 critério a reconciliar (provável desdobramento dentro de Cisne Negro ou Macro). Marcado como pendência: ao subir o doc-mestre markdown, substituir esta tabela pela versão verbatim e travar em 34.
