# Essencial Skills

Plugins e skills para o Claude, focados em negócios, finanças, direito, escrita e produtividade no Brasil.

## Plugins

| Plugin | O que faz |
|---|---|
| [super-assessor-juridico](plugins/super-assessor-juridico) | Assessoria jurídica brasileira baseada em dados e orientada à conciliação: triagem de prazo, score de viabilidade com chance de êxito e valores, negociação estratégica e redação jurídica em linguagem simples. Inclui 3 skills. |

## Skills

| Skill | Área | O que faz |
|---|---|---|
| [paul](skills/paul) | Projetos | Conduz projetos pelo ciclo Planejar, Aplicar, Unificar, com entrevista, critérios de aceite e verificação |
| [mentor-de-negocios](skills/mentor-de-negocios) | Negócios | Valida ideias, diagnostica empresas com problema e monta plano de negócios com viabilidade |
| [modelagem-financeira](skills/modelagem-financeira) | Finanças | Modelo financeiro em Excel: DRE, fluxo de caixa, ponto de equilíbrio, payback e retorno contra a SELIC |
| [analise-antifragil](skills/analise-antifragil) | Investimentos | Score de 0 a 100 e alocação antifrágil para ativos e carteiras |
| [roteiro-vendas-7-passos](skills/roteiro-vendas-7-passos) | Vendas | Roteiro de call consultiva de alto ticket |
| [copywriter-01-principiosdestrunkwhite](skills/copywriter-01-principiosdestrunkwhite) | Escrita | Textos e copy de conversão com Strunk & White e as sete varreduras de revisão |
| [comunicacao-interna](skills/comunicacao-interna) | Gestão | Comunicados, update semanal 3P, informativo, FAQ e update para sócios |
| [coautoria-de-documentos](skills/coautoria-de-documentos) | Escrita | Escrita a quatro mãos de propostas, estudos e relatórios, com teste de leitor |
| [editor-literario](skills/editor-literario) | Livros | Revisão editorial em 7 níveis para originais de livro |
| [super-professor](skills/super-professor) | Aprendizado | Ensina qualquer assunto do básico ao avançado, com plano de estudos |

## Como instalar

**Skill avulsa no app do Claude:** compacte a pasta da skill em .zip e envie nas configurações de skills do Claude.

**Plugin no app do Claude:** compacte o conteúdo da pasta do plugin, renomeie para `.plugin` e abra no Claude.

**No Claude Code:**

```
/plugin marketplace add tmxc21/essencial-skills
/plugin install super-assessor-juridico@essencial-skills
```

## Aviso

Ferramentas de apoio. Não substituem advogado, contador, consultor de investimentos ou outro profissional habilitado.
