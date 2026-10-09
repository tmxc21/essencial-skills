---
name: coautoria-de-documentos
description: "Conduz a escrita a quatro mãos de documentos estruturados (proposta comercial, contrato a revisar, plano, estudo, relatório para sócio ou investidor, especificação, documento de decisão, manual, SOP) em três etapas: coleta de contexto, construção seção por seção e teste com leitor sem contexto. Use quando o usuário disser \"vamos escrever um documento\", \"me ajuda a montar uma proposta\", \"preciso redigir um plano/estudo/relatório\", \"escreve comigo\", ou começar uma tarefa de escrita longa que outras pessoas vão ler. NÃO usar para texto curto de venda (copywriter), comunicado à equipe (comunicacao-interna) nem livro (editor-literario)."
---

# Coautoria de documentos

Adaptada da skill doc-coauthoring da Anthropic. Você guia o usuário em três etapas: Contexto, Construção e Teste de leitor. O objetivo é um documento que funcione para quem vai ler, inclusive quando essa pessoa colar o documento no Claude para entender.

Siga regras-de-resposta (idioma e sem travessão) e os princípios da copywriter. Uma pergunta por vez, sempre com a sua sugestão de resposta.

## Abertura

Explique as três etapas em três linhas e pergunte se ele quer seguir o fluxo ou escrever livre. Se escolher livre, escreva livre.

## Etapa 1: Contexto

Objetivo: fechar a distância entre o que o usuário sabe e o que você sabe.

1. Antes de perguntar, procure: memória do usuário, arquivos anexados, Drive, e-mail e agenda conectados.
2. Confirme, uma por vez, só o que faltar:
   - Tipo de documento.
   - Quem lê e o que essa pessoa precisa decidir ou fazer depois de ler.
   - Modelo ou formato obrigatório.
   - Prazo e restrições.
3. Peça um despejo de informação: ele pode mandar tudo bagunçado, em áudio transcrito, prints, links. Não precisa organizar.
4. Depois do despejo, faça perguntas sobre as lacunas, uma por vez, começando pela que mais muda o documento.
5. A etapa termina quando suas perguntas já são sobre trade-offs e casos de borda, não sobre o básico. Pergunte se há mais contexto antes de seguir.

## Etapa 2: Construção

1. Proponha a estrutura (3 a 6 seções adequadas ao tipo) e confirme.
2. Crie o documento com todas as seções e um marcador "[a escrever]" em cada. Use o tipo de artefato Docs se estiver disponível; senão, um arquivo .md ou .docx conforme o pedido.
3. Comece pela seção com mais incógnitas (em proposta, normalmente a solução e o preço; em estudo, a conclusão). Resumo executivo fica por último.
4. Para cada seção:
   1. **Pergunta:** o que precisa estar nela (uma por vez).
   2. **Ideias:** liste de 5 a 15 itens numerados que poderiam entrar, incluindo contexto que ele deu e pode ter esquecido.
   3. **Curadoria:** ele indica o que manter, cortar ou juntar ("mantém 1, 4, 7; corta 3; junta 5 e 6"). Resposta livre também vale; extraia as preferências.
   4. **Lacuna:** pergunte se falta algo importante.
   5. **Redação:** escreva só aquela seção, substituindo o marcador.
   6. **Ajuste:** peça que ele diga o que mudar em vez de editar direto, para você aprender o estilo dele. Edite pontualmente, sem reescrever o documento inteiro.
   Depois de três rodadas sem mudança relevante, pergunte se dá para cortar algo sem perder informação.
5. Com 80% das seções prontas, releia o documento inteiro procurando incoerência, repetição, contradição e enchimento genérico.

## Etapa 3: Teste de leitor

Objetivo: descobrir o que só faz sentido para quem escreveu.

1. Liste de 5 a 10 perguntas que o leitor real faria ao documento.
2. Se houver subagentes disponíveis, teste você mesmo: passe só o documento e cada pergunta a um agente sem contexto. Peça também que aponte ambiguidades, suposições não explicadas e contradições.
3. Sem subagentes, oriente o usuário: abrir uma conversa nova no Claude, colar o documento, fazer as perguntas e trazer as respostas.
4. Onde o leitor errou ou travou, volte à seção e corrija.
5. O documento está pronto quando o leitor sem contexto responde certo e não aponta lacunas novas.

## Fechamento

1. Recomende que ele faça uma leitura final: o documento é dele.
2. Peça que confira números, nomes, datas e links.
3. Confirme se o documento cumpre o objetivo definido na Etapa 1.
