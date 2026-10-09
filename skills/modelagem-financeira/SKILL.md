---
name: modelagem-financeira
description: Constrói um modelo financeiro completo em Excel (.xlsx) para negócios no Brasil — serve tanto para negócio novo/pré-operação (projeção de receita, DRE projetada, ponto de equilíbrio, payback, retorno vs SELIC) quanto para negócio em operação (DRE real, fluxo de caixa, unit economics, margem por produto). Use sempre que o usuário pedir para modelar/projetar finanças de um negócio, montar DRE, calcular ponto de equilíbrio, fluxo de caixa, unit economics, margem, payback ou retorno de um investimento, comparar o retorno de um negócio com a renda fixa, ou disser algo como "quanto preciso vender pra empatar", "esse negócio se paga em quanto tempo", "monta uma planilha financeira". O resultado é sempre um arquivo .xlsx editável, com premissas separadas em azul e fórmulas dinâmicas. NÃO usar quando o pedido é só análise qualitativa em prosa (isso é a skill de mentor-de-negócios) nem para simples limpeza de planilha existente.
---

# Modelagem Financeira (Brasil)

Gera um modelo financeiro em Excel editável e dinâmico. A mecânica de criação do arquivo (openpyxl, recálculo com LibreOffice, verificação de erros) segue **integralmente o skill `xlsx`** — leia e siga o SKILL.md dele para construir e validar o arquivo. Este skill define a **estrutura financeira e as convenções brasileiras** que vão dentro do modelo.

## Regras de ouro
- **Premissas separadas, em azul** (RGB 0,0,255). Toda taxa, preço, volume e custo unitário fica numa aba/bloco de Premissas. Fórmulas em preto referenciam essas células — nunca hardcode valor dentro de fórmula.
- **Zero erro de fórmula.** Rodar `scripts/recalc.py` do skill xlsx e corrigir qualquer #REF!, #DIV/0!, #VALUE! antes de entregar.
- **Moeda em R$**, formato `R$ #,##0`; zeros como "-"; negativos entre parênteses; percentuais com uma casa.
- **Nunca inventar número.** SELIC, alíquotas de imposto e benchmarks de mercado devem vir de busca na web (web_search) com a fonte anotada em comentário na célula. Se o usuário não deu um dado, pergunte — uma pergunta por vez — em vez de chutar.
- Se faltar dado do usuário, marque a célula com fundo amarelo (premissa a confirmar) e siga.

## Descobrir o cenário
Antes de construir, identifique (perguntando o que faltar, uma coisa por vez):
- É **pré-operação** (projeção) ou **negócio em operação** (dados reais)? Pode ser os dois no mesmo arquivo.
- Horizonte do modelo (padrão: 12 meses mensais + resumo anual; 3 anos se for avaliação de investimento).
- Investimento inicial (CAPEX + capital de giro), se houver.
- Modelo de receita (venda única, recorrência, ticket médio × volume).
- Regime tributário aproximado (Simples/Presumido) — impacta a alíquota sobre receita.

## Estrutura do arquivo (abas)

### 1. Premissas
Todas as entradas editáveis, em azul, agrupadas: preços/ticket, volumes, custos variáveis unitários, custos fixos mensais, alíquota de imposto sobre receita, investimento inicial, SELIC anual (com fonte), taxa de crescimento mensal. Fundo amarelo no que estiver por confirmar.

### 2. DRE (mensal + anual)
Ordem: Receita bruta → (−) impostos sobre receita → Receita líquida → (−) CPV/custo do serviço → **Lucro bruto** → (−) despesas operacionais (marketing, vendas, administrativas) → **EBIT** → (−/+) resultado financeiro → (−) IR/CSLL se aplicável → **Lucro líquido**. Linha de margem líquida (%) ao fim. Se for negócio em operação, a mesma estrutura recebe dados reais; se projeção, puxa das premissas.

### 3. Fluxo de caixa
Entradas e saídas por mês, saldo inicial, saldo final acumulado. Destacar meses de caixa negativo (necessidade de capital de giro). Relevante principalmente pro negócio em operação e pra fase inicial de pré-operação.

### 4. Unit economics
Por unidade/produto: preço, custo variável, **margem de contribuição** (R$ e %), e — quando fizer sentido — CAC, LTV e razão LTV/CAC. Para o negócio em operação, permite ver qual produto sustenta o resultado.

### 5. Ponto de equilíbrio
Custos fixos totais ÷ margem de contribuição unitária = volume de equilíbrio (unidades) e receita de equilíbrio (R$). Mostrar também a margem de segurança vs volume projetado/real.

### 6. Retorno vs SELIC (só se houver investimento)
- Payback (em meses) do investimento inicial.
- Retorno anualizado do negócio = lucro líquido anual ÷ investimento total.
- Comparação direta com a SELIC anual vigente (buscar valor atual e anotar fonte): o prêmio de risco justifica sair da renda fixa? Deixar essa conclusão explícita numa célula de texto.

## Fechamento
Depois de gerar e recalcular sem erros, entregue o .xlsx via present_files e resuma em 3–4 linhas os números-chave (break-even, margem líquida, payback e o veredito vs SELIC). Sem enrolação.
