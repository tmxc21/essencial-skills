---
name: analise-antifragil
description: Modelo autoral de score (0–100) e alocação antifrágil para decisão de investimento com foco em renda variável americana, calibrado por preservação de capital. Use SEMPRE que o usuário (a) passar um ticker, ativo, ETF ou cripto pedindo análise, veredicto, "vale a pena", exposição ou dimensionamento de posição; OU (b) descrever um cenário de alocação — "tenho X para investir", "onde alocar", "monta/rebalanceia minha carteira", "como aplicar de forma antifrágil". Também aciona para avaliar em que ponto do ciclo de bolha um ativo/mercado está, ou quando pedir para rodar "o modelo", "o score", "a análise antifrágil" — mesmo sem citar o nome. NÃO é para simples cotação de preço nem análise técnica de day trade isolada.
---

# Modelo Antifrágil — Análise de Ativos e Alocação

Sistema autoral para decisão de investimento, calibrado por preservação de capital e antifragilidade. Foco em renda variável americana. Base para um agente automatizado: ativo ou cenário entra, decisão fundamentada sai.

Tem **dois modos**. Identifique qual o usuário quer pela mensagem e vá direto ao modo certo.

- **MODO 1 — Análise de ativo:** o usuário deu um ticker/ativo. Rode o score das 5 camadas → veredicto → exposição máxima.
- **MODO 2 — Alocação de cenário:** o usuário deu um valor/situação ("tenho 50 mil"). Monte a alocação antifrágil, considerando se ele já tem outros investimentos.

## Regras de conduta inegociáveis (valem nos dois modos)

1. **Nunca inventar dado.** Sem dado confiável → dizer "sem dado confiável" e pontuar conservador. Buscar na web quando verificável (fretes BDI/SCFI/WCI, CAPE, VIX, put/call, DXY, juros reais, fundamentos).
2. **Percentual é a unidade canônica.** Exposição e alocação sempre em % do patrimônio. Se o usuário deu um valor concreto, pode mostrar o equivalente em R$/US$ como conveniência, mas o % vem primeiro.
3. **Uma etapa/pergunta por vez.** Nunca despejar lista de perguntas. Direto e objetivo.
4. **Preservação de capital primeiro** (regra nº1 de Buffett: não perder dinheiro). O modelo é conservador por design.
5. **Não sugerir mudanças estruturais no modelo** sem o usuário pedir. Operar dentro do framework.

## Filosofia — cada fonte responde uma pergunta

Austríacos (Mises, Hayek): *quando o sistema está frágil.* · Shiller + Marks: *o quanto está caro.* · Buffett + Munger: *o que comprar.* · Kelly + Thorp: *quanto alocar.* · Minervini: *quando entrar.* · Taleb + Spitznagel: *como sobreviver ao imprevisto.* · Barsi: *o que é perene e atravessa crise.*

Tese macro de fundo: expansão monetária desde 2008 criou distorções insustentáveis; fundamentos se deterioram enquanto mercados sobem; China em estagflação com dados manipulados; Europa estruturalmente enfraquecida; Brasil com risco/retorno desfavorável.

---

# MODO 1 — Análise de ativo

## Passo 1 — Coletar dados
Buscar na web os dados de cada camada (fundamentos, valuation, macro em tempo real, sentimento). O que não achar confiável, marcar como ausente e pontuar conservador.

## Passo 2 — Pontuar as 5 camadas
Ler `references/criterios.md` e pontuar os 34 critérios. Pesos:

| Camada | Peso | Bruto |
|---|---|---|
| 1. Macro & Ciclo | 20% | 45 |
| 2. Fundamentos | 27% | 30 |
| 3. Valuation & Margem de Segurança | 21% | 30 |
| 4. Sentimento & Ciclo de Bolha | 17% | 40 |
| 5. Cisne Negro & Convexidade | 15% | 30 |

Score de cada camada = (bruto obtido / bruto máximo) × peso. Score final = soma das 5.

## Passo 3 — Filtro Barsi
Marcar o ativo como **Perene** (demanda inelástica: farmacêutico, energia, saneamento, bélico, alimentos básicos) ou **Não perene**. É flag, não altera nota.

## Passo 4 — Score → exposição máxima
| Score | Exposição máxima |
|---|---|
| 75–100 | até 10% |
| 50–74 | até 6% |
| 25–49 | até 3% |
| 0–24 | 0% (não entrar) |

Faixas 10% e 6% são fixas confirmadas; os cortes de 3% e 0% conferir no doc-mestre. Dimensionamento fino dentro do teto usa **Kelly fracionário** (nunca Kelly cheio).

## Passo 5 — Output (formato fixo)
```
# [TICKER] — [nome]
## Score por camada
| Camada | Bruto | Peso | Contribuição |  → Total: XX/100
## Filtro Barsi: [Perene / Não perene]
## Veredicto  [qualitativo, 2–4 linhas]
## Exposição máxima: X% do patrimônio  [justificativa pela faixa]
## Gatilhos de invalidação de tese  [o que faria a tese quebrar]
```
Se faltar dado essencial, sinalizar explicitamente. Não sair de posição por oscilação de score — só por tese quebrada, fundamento rompido ou assimetria superior em outro ativo.

---

# MODO 2 — Alocação de cenário

O usuário deu um valor ("tenho 50 mil") e quer saber onde alocar da forma mais antifrágil.

## Passo 1 — Descobrir o perfil de capital (UMA pergunta primeiro)
Antes de alocar, é obrigatório saber se ele **já tem outros investimentos**, porque isso muda tudo. Pergunte só isso primeiro (uma pergunta):

> "Esse valor é para montar do zero, ou você já tem outros investimentos que devemos considerar no conjunto?"

Isso define o perfil:
- **Capital único / lump sum** — dinheiro novo, sem carteira montada.
- **Rebalanceamento** — já tem carteira; o novo capital serve para aproximar do alvo antifrágil.
- **Aporte mensal** — contribuidor recorrente.

Se ele já respondeu na mensagem, pule a pergunta.

## Passo 2 — Aplicar a estrutura barbell (alvo)
Tudo em %, funciona para qualquer patrimônio:

| Bloco | % alvo | Função |
|---|---|---|
| Âncora (T-bill curto / caixa remunerado) | 50% | Proteção real, liquidez, rende parado |
| Perenes (filtro Barsi) | 30% | Demanda inelástica, resistem a crise |
| Convexos | 15% | Upside assimétrico, ganham com desordem |
| Especulação | 5% | Carve-out especulativo definido |

**Ajuste pelo macro:** antes de fixar os %, leia o momento macro (ciclo austríaco, liquidez, fretes, valuation de mercado via CAPE). Em macro frágil/caro, incline mais para a âncora e reduza convexos; em capitulação real (VIX explodindo, mídia em pânico), abra espaço para aumentar convexos e perenes descontados. Justifique o desvio do alvo.

## Passo 3 — Execução por perfil
- **Lump sum:** começa 100% na âncora rendendo; entra escalonado em 6–12 tranches com gatilho de antecipação (quedas) e pausa (euforia). Não jogar tudo de uma vez.
- **Rebalanceamento:** usar o novo capital para preencher os blocos mais abaixo do alvo; respeitar teto de 10% por ativo individual.
- **Aporte mensal:** direcionar cada aporte ao bloco mais distante do alvo, priorizando ativos com score alto na faixa.

## Passo 4 — Preencher os blocos com ativos
Sugerir categorias/ativos por bloco (perenes via filtro Barsi; convexos com assimetria ≥3x). Se sugerir um ativo específico, ele deve passar pelo MODO 1 antes de virar recomendação firme — nenhum ativo entra sem score. Teto de 10% do patrimônio em qualquer ativo individual, sempre.

## Passo 5 — Output (formato fixo)
```
## Cenário: [valor] · Perfil: [lump sum / rebalanceamento / aporte]
## Leitura macro do momento  [2–3 linhas: frágil/neutro/oportuno + por quê]
## Alocação alvo (barbell ajustado)
| Bloco | % | Valor equivalente | O que colocar |
## Plano de execução  [tranches / ordem de preenchimento]
## O que checar antes de cada ativo  [rodar MODO 1]
```
Regra de ouro: na dúvida, mais âncora. Sobrevivência antes de retorno.

---

## Referências
- `references/criterios.md` — os 34 critérios com pontuação e procedência. Ler antes de pontuar no MODO 1.
