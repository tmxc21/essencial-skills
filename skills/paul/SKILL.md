---
name: paul
description: Conduz qualquer projeto ou tarefa de várias etapas pelo ciclo PAUL (Planejar, Aplicar, Unificar), com entrevista de requisitos, critérios de aceite, execução verificada e fechamento obrigatório. Use quando o usuário disser "PAUL", "/paul", "vamos planejar", "monta um plano e executa", "quero tirar esse projeto do papel", "me entrevista sobre isso", "grill me", "retoma o projeto X", ou trouxer um projeto com várias entregas (campanha, lançamento, site, processo, abertura de unidade, automação, documento grande). Substitui grill-me, grilling, brainstorming, writing-plans, executing-plans e verification-before-completion. NÃO usar para validar se uma ideia de negócio vale a pena (isso é mentor-de-negocios) nem para pergunta simples de resposta única.
---

# PAUL: Planejar, Aplicar, Unificar

Adaptação para o Claude (chat e Cowork) do framework PAUL de Christopher Kahler (github.com/ChristopherKahler/paul, v1.4.0), unificada com as técnicas de entrevista do grilling (Matt Pocock) e de planejamento e verificação do Superpowers (obra).

Todo trabalho passa pelo ciclo abaixo. Nenhum plano fica aberto: todo PLANEJAR termina em UNIFICAR.

```
INICIAR (uma vez) → PLANEJAR → APLICAR → UNIFICAR → próximo PLANEJAR
```

Três princípios:
1. **Ciclo fechado.** Todo plano termina com UNIFICAR. Plano órfão é proibido.
2. **Definir "pronto" antes de começar.** Critérios de aceite vêm antes da execução.
3. **Qualificar, não presumir.** Cada entrega é conferida contra o que foi pedido antes de ser dada como concluída.

## Regras de condução

- Uma pergunta por vez. Espere a resposta antes da próxima.
- Toda pergunta vem com a sua resposta recomendada, redigida para que "sim" aceite a recomendação.
- Fatos você descobre sozinho (arquivos, conectores, busca na web, memória). Decisões são do usuário.
- Linguagem direta, sem preâmbulo. Português do Brasil.
- Mostre em que ponto do ciclo você está no topo de cada fase:
  `PLANEJAR ✓ → APLICAR ○ → UNIFICAR ○`

## Onde o estado fica guardado

O PAUL precisa de memória entre sessões. Mantenha um **Painel do Projeto** com quatro blocos: PROJETO, ROTEIRO, ESTADO e DECISÕES.

- Se houver tipo de artefato Docs disponível, crie o painel como um Doc e atualize a cada fase.
- Senão, mantenha um arquivo `PAINEL-<projeto>.md` e envie ao usuário a cada UNIFICAR.
- Ao retomar ("retoma o projeto X"), localize o painel (artefatos, arquivos anexados, Drive conectado) antes de perguntar qualquer coisa. Só peça ao usuário se não achar.

Modelo do painel:

```markdown
# Painel: <nome do projeto>

## PROJETO
Objetivo: <resultado mensurável>
Para quem: <cliente ou público>
Restrições: <prazo, orçamento, ferramentas, o que não pode mudar>
Pronto quando: <critério final do projeto>

## ROTEIRO
| Fase | Entrega | Status |
|---|---|---|
| 1 | ... | concluída / em andamento / pendente |

## ESTADO
Posição no ciclo: PLANEJAR ✓ APLICAR ○ UNIFICAR ○
Fase atual: <n>
Próximo passo: <ação concreta>
Bloqueios: <nenhum ou descrição>

## DECISÕES
- <data>: <decisão> (motivo)
```

## Fase 0: INICIAR (só na primeira vez)

Objetivo: sair com PROJETO e ROTEIRO preenchidos com informação real, nunca com espaços em branco.

1. Identifique o tipo: negócio/operação, marketing/campanha, produto digital/site, documento/estudo, automação, outro. O tipo muda as perguntas.
2. Entreviste em **árvore de decisões**. A fronteira são as decisões cujos pré-requisitos já foram respondidos. Faça uma pergunta da fronteira por vez, com recomendação. Cada resposta libera as perguntas que dependiam dela.
3. Antes de perguntar, procure a resposta: memória do usuário, arquivos, conectores, web. Nunca pergunte o que dá para descobrir.
4. Perguntas típicas por tipo:
   - Negócio: resultado esperado em número, prazo, orçamento, quem executa, o que já existe.
   - Marketing: público, oferta, canal, meta (leads, vendas, alcance), orçamento de mídia, prova social disponível.
   - Site/produto: o que o usuário final faz, ação principal, referências, onde hospeda.
   - Documento/estudo: quem lê, que decisão o documento apoia, formato e prazo.
5. A entrevista termina quando a fronteira está vazia: nenhum ramo ficou presumido em silêncio. Resuma o entendimento e peça confirmação.
6. Monte o ROTEIRO em fases (de 2 a 6), cada uma com uma entrega verificável. Crie o painel.

## Fase 1: PLANEJAR

1. Confira o ESTADO. Se o ciclo anterior não foi unificado, avise e unifique antes.
2. Classifique o tamanho e confirme com o usuário:
   - **Rápido** (cabe em uma frase, uma entrega, sem decisão estrutural): objetivo + 1 tarefa + 1 critério.
   - **Padrão**: plano completo.
   - **Complexo** (6+ tarefas, várias áreas, decisões estruturais): plano completo e proposta de dividir em planos menores.
3. Escreva o plano:

```markdown
## Plano <fase>.<número>: <título>

**Objetivo:** <o que este plano entrega, mensurável>
**Por quê:** <como serve ao objetivo do projeto>
**Entrega:** <arquivos, artefatos, mensagens, ações>

### Critérios de aceite
- CA1: Dado <situação>, quando <ação>, então <resultado observável>
- CA2: ...

### Tarefas
1. **<tarefa>**
   Ação: <o que fazer, específico>
   Verificar: <como provar que ficou certo>
   Pronto quando: <ligado a CA1, CA2...>
2. ...

### Limites
Não mexer em: <o que fica intocado>
Fora do escopo: <o que não será feito agora>

### Pontos de checagem com o usuário
<onde parar e pedir aprovação, ex.: antes de enviar e-mail, publicar, gastar dinheiro>
```

4. Cheque coerência: o plano serve ao PROJETO? Contradiz alguma DECISÃO? Toda tarefa aponta para um critério? Todo critério tem tarefa?
5. **Pare e peça aprovação.** Não execute sem o "ok".
6. Atualize o ESTADO: `PLANEJAR ✓ → APLICAR ○ → UNIFICAR ○`.

## Fase 2: APLICAR

Para cada tarefa, rode o ciclo Executar/Qualificar:

```
EXECUTAR → INFORMAR STATUS → QUALIFICAR → (corrigir lacunas) → PRÓXIMA
```

1. **Executar** a ação descrita, usando as skills e ferramentas que a tarefa pedir (xlsx, docs, copywriter, modelagem-financeira, pesquisa etc.).
2. **Informar status**, um destes:
   - FEITO: concluído sem ressalvas.
   - FEITO COM RESSALVAS: concluído, mas há dúvida. Diga qual.
   - FALTA CONTEXTO: não dá para concluir sem informação. Pare e pergunte (uma pergunta).
   - BLOQUEADO: impedimento estrutural. Diga o que tentou, o que trava e que ajuda precisa.
   Nunca entregue em silêncio algo de que você duvida.
3. **Qualificar** de forma independente: releia o que foi produzido de verdade (abra o arquivo, rode a conta, confira o número na fonte). Não confie na lembrança de ter feito. Compare com a tarefa e o critério ligado. Nota:
   - OK: bate com o especificado.
   - LACUNA: faltou algo.
   - DESVIO: fez algo diferente do pedido.
   Lacuna ou desvio: corrija e requalifique. Depois de 3 tentativas, escale ao usuário.
4. Em ponto de checagem, pare e espere o usuário.
5. Se o usuário reprovar algo, classifique a causa antes de corrigir:
   - Intenção errada → volte ao PLANEJAR com a intenção atualizada.
   - Plano errado → corrija critérios e tarefas, depois a entrega.
   - Execução errada → corrija a entrega.
6. Registre desvios do plano à medida que acontecem.

Regra de verificação: nunca diga "pronto", "funciona" ou "concluído" sem evidência produzida nesta mesma fase (arquivo aberto, cálculo rodado, link testado).

## Fase 3: UNIFICAR (obrigatória)

1. Compare plano e execução, tarefa por tarefa.
2. Registre o resultado de cada critério: PASSOU ou FALHOU (com motivo).
3. Liste desvios e por que aconteceram.
4. Atualize o painel: ESTADO (posição, fase, próximo passo), ROTEIRO (status da fase) e DECISÕES (o que foi decidido e por quê).
5. Entregue ao usuário um resumo curto:

```markdown
## Unificação <fase>.<número>
Entregue: <lista curta>
Critérios: CA1 ✓ · CA2 ✓ · CA3 ✗ (<motivo>)
Desvios: <nenhum ou lista>
Próximo: <próximo plano sugerido>
```

6. Feche o ciclo: `PLANEJAR ✓ → APLICAR ✓ → UNIFICAR ✓`. Pergunte se segue para o próximo plano.

## Comandos que o usuário pode usar

- "PAUL iniciar <projeto>": Fase 0.
- "PAUL planejar": próximo plano do roteiro.
- "PAUL aplicar": executa o plano aprovado.
- "PAUL unificar": fecha o ciclo.
- "PAUL status": mostra o ESTADO e o próximo passo.
- "PAUL pausar": salva o painel com instruções de retomada.
- "PAUL retomar <projeto>": localiza o painel e continua de onde parou.
- "me entrevista sobre <tema>": só a entrevista em árvore da Fase 0, sem executar nada.

## Integração com outras skills

- Ideia ainda não validada: rode mentor-de-negocios antes e traga o resultado para o PROJETO.
- Números, DRE, ponto de equilíbrio: tarefa que chama modelagem-financeira.
- Textos e páginas de venda: tarefa que chama copywriter.
- Toda resposta segue regras-de-resposta.
