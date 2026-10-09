# Modelo de score de viabilidade

Objetivo: transformar fatos, provas, defesa provável e precedentes em uma diretriz numérica. É estimativa marginal, nunca promessa. Mostre sempre as premissas para o usuário poder ajustar.

## 1. Notas por pilar (0 a 10, com o motivo em uma linha)

| Pilar | Peso | 0 a 3 | 4 a 6 | 7 a 10 |
|---|---|---|---|---|
| Provas | 30 | Só o relato | Testemunhas, prints sem verificação, indícios | Documentos (contrato, nota, e-mail com cabeçalho, ata notarial, laudo) |
| Precedentes | 25 | Precedente obrigatório contra, ou TJ local majoritariamente contra | Jurisprudência dividida ou escassa | Precedente obrigatório a favor, ou TJ local majoritariamente a favor |
| Fatos e fundamento | 20 | Direito duvidoso ou sem nexo entre fato e dano | Direito existe, nexo discutível | Direito claro, nexo direto, dano demonstrável |
| Defesa provável (inverso) | 15 | Defesa forte (prescrição, culpa exclusiva, cumprimento) | Defesa razoável | Defesa fraca ou inexistente |
| Viabilidade prática | 10 | Prazo crítico, outra parte sem patrimônio, cobrança difícil | Riscos moderados | Prazo folgado, outra parte solvente |

**Score** = soma de (nota × peso ÷ 10). Resultado de 0 a 100.

## 2. Chance de êxito (faixa)

Parta da taxa de vitória observada nos precedentes parecidos e ajuste pelo score:

| Score | Ajuste sobre a taxa observada |
|---|---|
| 80 a 100 | +10 a +15 pontos percentuais |
| 60 a 79 | 0 a +10 |
| 40 a 59 | −10 a 0 |
| 0 a 39 | −25 a −10 |

Sem taxa observada confiável, use faixa larga (amplitude mínima de 20 pontos) e diga isso. Nunca apresente número único.

## 3. Valores (sempre em faixa, em reais)

- **Ganho provável (G):** faixa de valores fixados nos precedentes parecidos, corrigida pela regra vigente (Lei 14.905/2024: correção pelo IPCA e juros pela SELIC menos IPCA; confirmar índices atuais por busca).
- **Custos próprios (C):** custas, perícia, honorários contratuais, deslocamentos.
- **Perda se perder (P):** honorários de sucumbência de 10% a 20% do valor da causa (CPC art. 85), custas da outra parte e, se for o caso, multa por litigância de má-fé (CPC art. 81).
- **Chance (p):** ponto médio da faixa de chance, usado só no cálculo.

**Valor esperado da ação (VE)** = p × G − (1 − p) × P − C

**Vale a pena (%)** = VE ÷ G. Compare com o retorno do mesmo valor na SELIC durante o tempo médio do processo no tribunal. Se o VE for menor que esse retorno, a ação não compensa financeiramente, e diga isso.

**Custo de não fazer nada:** prejuízo que continua correndo, perda do prazo, efeito de precedente (outros cobrarem o mesmo) e impacto reputacional. Estime em reais quando possível.

## 4. Parâmetros de acordo

- **Ataque, acordo mínimo aceitável:** VE líquido. Abaixo disso, a via judicial compensa mais. Proposta de abertura acima desse valor (ver negociacao-estrategica).
- **Defesa, acordo máximo aceitável:** valor esperado da condenação mais custos de defesa. Acima disso, defender compensa mais.
- Acordo rápido tem valor: inclua o ganho de tempo (meses × SELIC) e a eliminação do risco.

## 5. Regra de decisão

| Score | Diretriz |
|---|---|
| 0 a 39 | Não recomenda ação. Acordo ou preservação de provas. Se insistir, alerta registrado. |
| 40 a 69 | Acordo primeiro; via judicial como plano B. |
| 70 a 100 | Acordo com proposta firme; sem acordo, via judicial. |

Em todos os casos a conciliação é apresentada primeiro.

## 6. Formato de saída

```
SCORE DE VIABILIDADE: 72/100
Provas 8 (contrato e e-mails) · Precedentes 7 (TJPR majoritário a favor) · Fatos 8 · Defesa 6 · Viabilidade 7
Chance estimada: 65% a 75%
Ganho provável: R$ X a R$ Y
Risco se perder: R$ Z
Valor esperado: R$ W · Vale a pena: N% · SELIC no período: R$ S
Custo de não fazer nada: R$ ...
Acordo mínimo aceitável: R$ ... · Proposta de abertura: R$ ...
Premissas: ...
Estimativa técnica baseada nos dados coletados. Não é garantia de resultado.
```
