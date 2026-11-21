# 📓 LOGBOOK AFP — Algoritmos e Programação (2026.2)

> **Como usar este arquivo:** copie-o para a raiz do **seu** repositório (ou para `logbook/LOGBOOK.md`) e preencha **direto no GitHub** (botão ✏️ *Edit this file*) ou no VS Code. Ele reúne todos os instrumentos do Protocolo AFP 2026.2 (Logbook Individual — Campos 01 a 04, 06 e 07; Registro de Revisão por Pares — Campo 05; Checkpoint Conceitual; Rubrica de Defesa Técnica).
>
> **Organização:** o Logbook está dividido em **3 grupos de entrega**, cada um com seu prazo. Dentro de cada grupo, os **ciclos de entrega (01 a 12)** continuam os mesmos, com as orientações de preenchimento. Siga a ordem: **Grupo 1 → Grupo 2 → Grupo 3 → Defesa Técnica**.
>
> O `Diario.md` do checklist passa a ser **este arquivo**: o registro de cada ciclo está na seção do ciclo correspondente.

## 📍 Navegação rápida

| Seção | Prazo |
|---|---|
| [👨‍🎓 Identificação](#-identificação) | Hoje |
| [🟢 Grupo 1](#-grupo-1--prazo-segunda-1611-às-23h59) · Registros 01–04, Campos 01 e 02 | **Segunda 16/11, 23h59** |
| [🟠 Grupo 2](#-grupo-2--prazo-sábado-2111-às-23h59) · Registros 05–08, Checkpoint, Campos 03 e 04 | **Sábado 21/11, 23h59** |
| [🔵 Grupo 3](#-grupo-3--prazo-quinta-2611-às-23h59) · Registros 09–12, Campos 05, 06 e 07 | **Quinta 26/11, 23h59** |
| [🏁 Defesa Técnica](#-defesa-técnica--quarta-1811) | **Quarta 18/11** |
| [🆘 Estou atrasado](#-estou-atrasado-no-logbook-e-agora) | — |

---

## 👨‍🎓 Identificação

| Campo | Preencha |
|---|---|
| **Nome do estudante** | Pedro Lucas Pereira Rolim |
| **Curso / Módulo** | Sistemas de Informação, 2º período |
| **Unidade curricular** | Algoritmos e Programação — UnDB 2026.2 |
| **Professor** | Rondineli Seba Salomão |
| **App-base do meu CRUD** | Catálogo de filmes e séries |
| **Link do meu repositório** | https://github.com/pedruck9-crypto/algoritmos-e-programacao |
| **Dupla de revisão (Campo 05)** | Pedro Henrique (nome no GitHub: Venancio Sampaio) |
| **Função neste ciclo** | Autor do meu CRUD e revisor do CRUD de um colega |

---

## 🧭 Regras de ouro (leia antes de preencher)

1. **Processo, não resultado.** O Logbook mostra *como você pensou*, não só o que funcionou. Registre erros, desvios e dúvidas reais.
2. **Vocabulário técnico.** Use os termos da área (ex.: "laço de repetição", "validação de entrada", "estrutura de dados"). Respostas genéricas ("aprendi Python") não são aceitas.
3. **Todo registro relevante tem 3 âncoras:** o **objeto de conhecimento** mobilizado + a **justificativa técnica** + a **referência/fonte**. *Decisão sem objeto de conhecimento e sem referência é considerada não rastreável e não conta para a avaliação formativa.*
4. **Coerência entre campos.** O Campo 02 deve ser coerente com o Campo 01. *Incoerência é evidência de autoria externa.* O Campo 07 retoma o Campo 01.
5. **IA é permitida e avaliada (Campo 04).** *Print sem análise crítica = devolução imediata. Reproduzir a IA sem questionamento = reprovado.* Você precisa mostrar o que aceitou **e** o que questionou/descartou, com argumento técnico.
6. **O histórico do Git é a sua evidência.** Faça commits pequenos e frequentes. Nunca reescreva o histórico (`force push`) do arquivo do Logbook.
7. **Campo 01 e Checkpoint são "sem consulta".** Preencha em um bloco contínuo, sem internet, sem material e sem colegas, no tempo indicado (Campo 01: durante o laboratório; Checkpoint: 20 min). Depois **não edite** esses campos — se perceber um erro, corrija em um campo posterior (Campo 03 ou 07), explicando.
8. **Os prazos dos grupos (16/11, 21/11 e 26/11, às 23h59)** valem para o commit no GitHub. O horário do commit é o registro oficial.

### ✅ Padrão de commit do Logbook

```text
docs(logbook): campo 01 — ciclo 02
docs(logbook): registro do ciclo 05
docs(logbook): campo 05 — revisão do CRUD de <colega>
```

---

## 🗓️ Calendário de entregas e Defesa

Os grupos têm **5 dias entre um prazo e outro**. O horário do commit no GitHub é o registro oficial.

| Grupo | Janela de preenchimento | **Prazo** | O que entregar |
|:--:|---|---|---|
| **1** | Qua 11/11 → seg 16/11 | **Segunda 16/11, 23h59** | Identificação · Registros dos Ciclos 01 a 04 · Campo 01 · Campo 02 |
| **2** | Seg 16/11 → sáb 21/11 | **Sábado 21/11, 23h59** | Registros dos Ciclos 05 a 08 · Checkpoint Conceitual · Campo 03 · Campo 04 |
| **3** | Sáb 21/11 → qui 26/11 | **Quinta 26/11, 23h59** | Registros dos Ciclos 09 a 12 · Campo 05 (2 revisões) · Campo 06 · Campo 07 |
| 🏁 | — | **Quarta 18/11** | **Defesa Técnica individual** (Rubrica) |

### Linha do tempo

| Data | Evento |
|---|---|
| Qua 11/11 | **Hoje:** começa o Grupo 1 |
| Seg 16/11 | ✅ Prazo do **Grupo 1** |
| **Qua 18/11** | 🏁 **Defesa Técnica** |
| Sáb 21/11 | ✅ Prazo do **Grupo 2** |
| Qua 25/11 | Avaliação P2 |
| Qui 26/11 | ✅ Prazo do **Grupo 3** |
| Qua 02/12 | Avaliação Substitutiva |
| Qua 09/12 | Avaliação Final |

> ⚠️ **Atenção:** a Defesa Técnica (18/11) acontece **antes** dos prazos dos Grupos 2 e 3. Na defesa você será arguido sobre **o que já estiver registrado e commitado**. Veja a seção [Defesa Técnica](#-defesa-técnica--quarta-1811) para saber o que priorizar até 18/11.

### Ciclos de entrega por grupo

| Ciclo | Data da aula | Tema do ciclo | Grupo | O que preencher |
|:--:|:--:|---|:--:|---|
| 01 | 12/08 | Preparação do laboratório e escolha do projeto | **1** | Registro do Ciclo |
| 02 | 19/08 | Variáveis, tipos de dados, entrada/saída | **1** | Registro + **Campo 01** + **Campo 02** |
| 03 | 26/08 | Operadores, fluxogramas, paradigmas | **1** (registro) · **2** (campos) | Registro (G1) · **Checkpoint**, **Campo 03**, **Campo 04** (G2) |
| 04 | 02/09 | Condicionais: `if`, `elif`, `else` | **1** | Registro do Ciclo |
| 05 | 09/09 | Condicionais aninhadas e operadores lógicos | **2** | Registro do Ciclo |
| 06 | 30/09 | Repetição: `for`, `while`, `break`, `continue` | **2** | Registro do Ciclo (inclui devolutiva da P1) |
| 07 | 07/10 | Listas: armazenamento e iteração | **2** | Registro do Ciclo |
| 08 | 14/10 | Busca e introdução a dicionários/matrizes | **2** | Registro do Ciclo |
| 09 | 21/10 | Atualização e exclusão: CRUD completo | **3** | Registro + **Campo 05** (revisão nº 1) |
| 10 | 28/10 | Modularização: funções | **3** | Registro do Ciclo |
| 11 | 04/11 | Recursividade | **3** | Registro + **Campo 06** |
| 12 | 11/11 | Refatoração e qualidade de código | **3** | Registro + **Campo 05** (revisão nº 2) + **Campo 07** |

---

## 📊 Painel de acompanhamento

Atualize a cada commit (troque ⬜ por ✅).

| Grupo | Item | Prazo | Preenchido | Commit |
|:--:|---|---|:--:|:--:|
| 1 | Identificação | 16/11 | ✅ | [Histórico](https://github.com/pedruck9-crypto/algoritmos-e-programacao/commits/main/LOGBOOK_AFP_Algoritmos_Programacao_2026-2.md) |
| 1 | Registros dos Ciclos 01, 02, 03 e 04 | 16/11 | ✅ | [Histórico](https://github.com/pedruck9-crypto/algoritmos-e-programacao/commits/main/LOGBOOK_AFP_Algoritmos_Programacao_2026-2.md) |
| 1 | Campo 01 — Instrumento de entrada | 16/11 | ✅ | [Histórico](https://github.com/pedruck9-crypto/algoritmos-e-programacao/commits/main/LOGBOOK_AFP_Algoritmos_Programacao_2026-2.md) |
| 1 | Campo 02 — Aprofundamento | 16/11 | ✅ | [Histórico](https://github.com/pedruck9-crypto/algoritmos-e-programacao/commits/main/LOGBOOK_AFP_Algoritmos_Programacao_2026-2.md) |
| 2 | Registros dos Ciclos 05, 06, 07 e 08 | 21/11 | ✅ | Registrados em 21/11/2026; devolutiva da P1 pendente |
| 2 | Checkpoint Conceitual | 21/11 | Pendente de orientação | Pendência registrada em 21/11/2026 |
| 2 | Campo 03 — Execução e desvios | 21/11 | Rascunho | Confirmar adequação do item 3b |
| 2 | Campo 04 — Interação com IA | 21/11 | ✅ | Interação em 16/11/2026, registro em 17/11/2026 |
| 3 | Registros dos Ciclos 09, 10, 11 e 12 | 26/11 | ⬜ | ⬜ |
| 3 | Campo 05 — Revisão por pares nº 1 e nº 2 | 26/11 | ⬜ | ⬜ |
| 3 | Campo 06 — Próximos passos | 26/11 | ⬜ | ⬜ |
| 3 | Campo 07 — Evolução conceitual | 26/11 | ⬜ | ⬜ |
| 🏁 | Defesa Técnica | 18/11 | ⬜ | — |

---

## ❓ A questão-problema da AFP

**Título:** *O sistema em produção: diagnosticando as falhas do CRUD que você mesmo construiu.*

> **Enunciado completo (Apêndice A):** _professor(a): cole aqui o enunciado e os anexos liberados conforme o cronograma._

A questão-problema é **a mesma durante todo o semestre**: ela se aplica ao **seu** CRUD, que cresce a cada ciclo. Os **dados com defeito** do seu app chegam em um **lote cumulativo único** e vão expondo problemas diferentes conforme sua estrutura evolui. Seu trabalho é diagnosticar, ajustar o CRUD para tratar cada falha e **registrar o raciocínio** neste Logbook.

---

# 🔁 REGISTRO DO CICLO — modelo (copie em cada ciclo)

Cada ciclo tem sua própria seção abaixo, já com o modelo. Se precisar de espaço extra, acrescente linhas.

```markdown
### Registro do Ciclo NN — DD/MM
1. **Desafio do ciclo (em 1 frase):**
2. **O que implementei (commits / arquivos / links):**
3. **Objeto(s) de conhecimento mobilizado(s) (vocabulário técnico):**
4. **Desvio ou erro encontrado + causa técnica:**
5. **Decisão de ajuste + fonte (livro, doc, vídeo, colega, IA):**
6. **Feedback recebido (professor/colega) e o que mudei por causa dele:**
7. **Próximo passo:**
```

**Como preencher bem:** escreva como se explicasse a um colega que não esteve na aula. O item 3 e o item 5 são os mais importantes: eles ligam o que você fez ao **conteúdo** e à **fonte**.

| ❌ Fraco | ✅ Forte |
|---|---|
| "Aprendi a usar `if`." | "Usei estrutura condicional aninhada para validar a idade antes de cadastrar. Meu erro foi comparar `str` com `int` (resultado de `input()`); corrigi com `int()` (Pense em Python, cap. 2)." |
| "Deu erro e consertei." | "O programa quebrou com `ZeroDivisionError` ao calcular a média de um item sem avaliações. Causa: divisão por `len(lista)` com lista vazia. Ajuste: testar `if len(lista) > 0`." |

---

# 🟢 GRUPO 1 — prazo segunda 16/11 às 23h59

> **Janela:** quarta 11/11 → segunda 16/11. **O que entregar:** Identificação · Registros dos Ciclos 01, 02, 03 e 04 · Campo 01 · Campo 02.
>
> **Sugestão de ordem:** (1) Identificação → (2) **Campo 01 primeiro, sem consulta** → (3) Registros dos Ciclos 01 a 04 → (4) Campo 02, com pesquisa.

**Checklist do Grupo 1**
- [ ] Identificação preenchida (app-base, link do repositório, dupla de revisão)
- [ ] Campo 01: 3 objetos de conhecimento, 3 lacunas, hipótese de até 5 linhas
- [ ] Registros dos Ciclos 01, 02, 03 e 04 com os 7 itens
- [ ] Campo 02: 2 referências com contribuição, hipótese revisada, 3 recursos
- [ ] Commits no GitHub e painel atualizado

## 🟢 CICLO 01 — 12/08 — Preparação do laboratório e escolha do projeto

<details>
<summary>📘 Orientações do Ciclo 01</summary>

- **Hoje não há Campo do Protocolo.** O foco é preparar o ambiente: criar o repositório, configurar o VS Code e escolher o **app-base** do seu CRUD (e, portanto, o *schema* dos seus dados).
- Preencha a **Identificação** (no início deste arquivo) e o **Registro do Ciclo 01**.
- No item 3, registre **o que você já sabia** e o que era novo (Git, GitHub, VS Code). Isso será útil para o Campo 07.
- No item 4, registre qualquer problema de instalação ou configuração e como o resolveu — isso conta como desvio.
- Faça o primeiro commit: `docs(logbook): registro do ciclo 01`.
</details>

#### Registro do Ciclo 01 — 12/08

1. **Desafio do ciclo (em 1 frase):** Escolher um tema para o meu CRUD e preparar o ambiente para começar a desenvolvê-lo.
2. **O que implementei (commits / arquivos / links):** Escolhi criar um catálogo de filmes e séries. Usei o GitHub para versionar o código. A primeira versão de terminal ficou registrada no arquivo [`crud_filmes_e_series.py` na branch `ciclo-1--terminal`](https://github.com/pedruck9-crypto/algoritmos-e-programacao/blob/ciclo-1--terminal/crud_filmes_e_series.py).
3. **Objeto(s) de conhecimento mobilizado(s):** Organização do projeto, definição dos dados do catálogo e uso de ferramentas de desenvolvimento. Antes da disciplina, meu conhecimento de Python era básico. Fui aprendendo sobre Python, GitHub e VS Code ao longo do semestre.
4. **Desvio ou erro encontrado + causa técnica:** Minha dificuldade inicial foi transformar o tema em algo que eu pudesse implementar. Eu ainda precisava definir quais informações representariam cada mídia. Durante a preparação do ambiente, não encontrei problemas de instalação ou configuração.
5. **Decisão de ajuste + fonte:** Escolhi filmes e séries porque já gostava do assunto. Na versão de terminal, organizei cada mídia em título, tipo, gênero, ano e sinopse. A escolha levou em conta a orientação oral do professor Rondineli Seba Salomão de evitar o tema de cadastro de biblioteca.
6. **Feedback recebido e o que mudei:** Considerei a orientação do professor sobre a escolha do tema e optei por um catálogo de filmes e séries.
7. **Próximo passo:** Definir quais dados o usuário vai digitar e experimentar como recebê-los e exibi-los em Python.

## 🟢 CICLO 02 — 19/08 — Variáveis, tipos de dados e entrada/saída

<details>
<summary>📘 Orientações do Ciclo 02 — Campo 01 (sem consulta) e Campo 02 (pesquisa)</summary>

**Campo 01 — Instrumento de entrada** · *sem consulta · faça primeiro*
- Preencha **antes de tudo**, em um bloco contínuo de cerca de 15 minutos, sem internet, sem material, sem IA e sem colegas, depois de conhecer a questão-problema e a primeira amostra de dados do seu app. Depois do Campo 01 você pode consultar o que quiser.
- **1a.** Liste pelo menos **3 objetos de conhecimento** que você acha que precisa dominar para resolver o problema. Use o vocabulário técnico da área. *Não precisa acertar tudo — o Campo 07 vai mostrar o quanto você evoluiu.*
- **1b.** Liste pelo menos **3 lacunas**: o que você **não sabe** e precisa descobrir, com precisão (ruim: "não sei programar"; bom: "não sei como validar a entrada para impedir que o usuário digite texto onde espero número").
- **1c.** Escreva sua **hipótese inicial** em até 5 linhas: o que você acha que está causando as falhas do CRUD e por quê.
- Faça o commit **logo ao terminar**. Depois, **não edite** o Campo 01.

**Campo 02 — Aprofundamento** · *AV Qualis · segunda 16/11, 23h59*
- Preencha **depois do Campo 01, com pesquisa real**, e seja coerente com ele.
- **2a.** Pelo menos **2 referências** (livro, documentação, vídeo, artigo), cada uma com a **contribuição** concreta para a sua solução. Não basta listar o título.
- **2b.** **Hipótese revisada:** o que mudou em relação ao Campo 01 e **por quê**. Se não mudou nada, explique por que a pesquisa confirmou a hipótese.
- **2c.** **Dimensionamento inicial de recursos** (mínimo 3 itens), com quantidade estimada e justificativa técnica. Exemplos de recursos no seu contexto: horas de estudo, número de casos de teste, módulos/arquivos do projeto, dados de teste, bibliotecas.
</details>

### 🧩 CAMPO 01 — Instrumento de entrada
*Grupo 1 | Prazo segunda 16/11, 23h59 | SEM CONSULTA*

**1a. Objetos de conhecimento identificados (mínimo 3, com vocabulário técnico):**

1. Estruturas condicionais (`if`, `elif` e `else`) para decidir o que fazer com a opção digitada.
2. Laço `while` para permitir ao usuário executar as operações pelo terminal.
3. Listas para guardar os registros do catálogo.

**1b. Lacunas — o que não sei e preciso descobrir (mínimo 3, com precisão técnica):**

1. Como usar `else` para exibir uma mensagem quando a opção digitada não existe no menu?
2. Por que os dados guardados em uma lista se perdem ao fechar o programa?
3. Como evitar mídias duplicadas no catálogo?

**1c. Hipótese inicial em até 5 linhas — com lógica da área de formação:**

> Minha suspeita inicial era que uma opção fora do menu pudesse exibir uma mensagem de erro e encerrar o menu indevidamente. Suspeitava que a lógica das condições pudesse encaminhar essa entrada para o mesmo bloco da opção `0`, acionando o `break`.

### 🧩 CAMPO 02 — Aprofundamento pós-aula
*AV Qualis — Grupo 1 | Segunda 16/11, 23h59*

> **Preenchido depois do Campo 01, com pesquisa real. Deve ser coerente com o Campo 01. Incoerência = evidência de autoria externa.**

**2a. Aprofundamento dos objetos de conhecimento (mínimo 2 referências com síntese da contribuição para a solução):**

- **Referência 1:** [Mais sobre listas](https://docs.python.org/pt-br/3/tutorial/datastructures.html#more-on-lists). **Contribuição:** A seção sobre `append()` me ajudou a entender como `midias.append(midia)` acrescenta uma mídia ao catálogo e mantém os registros anteriores. Pratiquei essa operação no exercício com ingredientes de um sanduíche com apoio do GitHub Copilot.
- **Referência 2:** [Salvando dados estruturados com JSON](https://docs.python.org/pt-br/3/tutorial/inputoutput.html#saving-structured-data-with-json). **Contribuição:** Os exemplos de `json.dump()` e `json.load()` me mostraram como gravar uma lista em um arquivo e recuperá-la em outra execução.

**2b. Hipótese revisada — o que mudou em relação ao Campo 01 e por quê:**

> No Campo 01, eu tinha dúvida sobre por que os registros do catálogo desapareciam ao fechar o programa. A pesquisa me ajudou a entender que a versão acadêmica de terminal guarda as mídias em uma lista na memória e inicia uma lista vazia a cada execução. Estudei como salvar e carregar os registros em um arquivo JSON, mas mantive os dados em memória para respeitar o escopo dessa versão.

**2c. Dimensionamento inicial de recursos (recurso, quantidade estimada, justificativa técnica — mínimo 3 itens):**

| RECURSO / MATERIAL / INSUMO | QUANTIDADE ESTIMADA | JUSTIFICATIVA TÉCNICA |
|---|---|---|
| Registros de exemplo | 2 mídias (1 filme e 1 série) | Verificar se o segundo cadastro é acrescentado à lista e se o primeiro continua aparecendo na listagem. |
| Casos de teste no terminal | 3 casos | Conferir a listagem de duas mídias, a rejeição de um título com apenas espaços e o que acontece com os registros ao fechar e reabrir o programa. |
| Tempo para executar e registrar os testes | 30 minutos | Estimei cerca de 10 minutos por caso para preparar a entrada, executar o teste e anotar o comportamento observado. |

#### Registro do Ciclo 02 — 19/08

1. **Desafio do ciclo (em 1 frase):** Ler os dados de um filme ou série pelo terminal e guardá-los em variáveis.
2. **O que implementei (commits / arquivos / links):** Usei `input()` para receber título, tipo, gênero, ano e sinopse e `print()` para exibir mensagens. A evidência está no arquivo [`crud_filmes_e_series.py` na branch `ciclo-1--terminal`](https://github.com/pedruck9-crypto/algoritmos-e-programacao/blob/ciclo-1--terminal/crud_filmes_e_series.py).
3. **Objeto(s) de conhecimento mobilizado(s):** Variáveis, entrada e saída pelo terminal, tipo `str` para os dados digitados e tipo `bool` para a variável `cadastrada`, que indica se já existe uma mídia cadastrada.
4. **Desvio ou erro encontrado + causa técnica:** Mesmo quando digito um ano como `2024`, o valor fica como texto porque `input()` devolve uma `str`. O programa consegue exibir o valor, mas precisaria convertê-lo antes de fazer uma comparação numérica.
5. **Decisão de ajuste + fonte:** Mantive o ano como texto nessa versão porque o programa apenas armazena e exibe o valor. Consultei a [documentação do Python sobre `input()`](https://docs.python.org/pt-br/3/builtins/functions.html#input) para confirmar o tipo devolvido pela função.
6. **Feedback recebido e o que mudei:** Não recebi feedback específico sobre este ciclo.
7. **Próximo passo:** Testar o cadastro com um ano válido e outro preenchido com letras para verificar se o campo precisa de validação.

## 🟢 CICLO 03 — 26/08 — Operadores, fluxogramas e paradigmas

<details>
<summary>📘 Orientações do Ciclo 03 — Registro (Grupo 1)</summary>

- Neste grupo você preenche **apenas o Registro do Ciclo 03**. O **Checkpoint Conceitual** e os **Campos 03 e 04** deste ciclo estão no **Grupo 2**.
- Item 3: nomeie os **operadores** (aritméticos, relacionais, lógicos) e os **tipos** que usou. Se montou fluxogramas, cite o que o fluxograma ajudou a perceber.
- Item 4: registre erros de precedência de operadores, divisão por zero ou confusão entre `=` e `==`, com a causa técnica.
</details>

#### Registro do Ciclo 03 — 26/08

1. **Desafio do ciclo (em 1 frase):** Usar operadores para interpretar a opção digitada no menu e encaminhar o usuário à operação correspondente.
2. **O que implementei (commits / arquivos / links):** Guardei a entrada na variável `opcao`. A expressão `opcao == "1"` verifica se a pessoa escolheu cadastrar uma mídia. Após um cadastro válido, `cadastrada = True` atualiza o estado do catálogo. Antes de escrever o menu, imaginei mentalmente a ordem dessas decisões. O código está em [`crud_filmes_e_series.py` na branch `ciclo-1--terminal`](https://github.com/pedruck9-crypto/algoritmos-e-programacao/blob/ciclo-1--terminal/crud_filmes_e_series.py).
3. **Objeto(s) de conhecimento mobilizado(s):** Comparação de igualdade (`==`), atribuição (`=`), tipo `str` para a opção digitada e tipo `bool` para o estado do cadastro.
4. **Desvio ou erro encontrado + causa técnica:** Não identifiquei um erro específico nesta etapa. Um cuidado foi comparar a opção com `"1"`, pois `input()` devolve texto. Se eu comparasse com o inteiro `1`, a condição seria falsa mesmo que o usuário tivesse digitado 1.
5. **Decisão de ajuste + fonte:** Usei `opcao == "1"` porque o valor digitado chega como texto. Quando a comparação dá `True`, o programa segue para o bloco de cadastro. Consultei [Comparações de valor](https://docs.python.org/pt-br/3/reference/expressions.html#value-comparisons) e a [documentação do Python sobre `input()`](https://docs.python.org/pt-br/3/builtins/functions.html#input).
6. **Feedback recebido e o que mudei:** Não recebi feedback específico para esta etapa.
7. **Próximo passo:** Testar uma opção válida e uma opção fora do menu para conferir o caminho seguido em cada caso.

## 🟢 CICLO 04 — 02/09 — Estruturas condicionais: `if`, `elif`, `else`

<details>
<summary>📘 Orientações do Ciclo 04</summary>

- **Sem Campo do Protocolo hoje.** Preencha o Registro do Ciclo 04.
- Conecte **cada condicional** do seu CRUD a uma **regra de negócio** (ex.: "preço não pode ser negativo").
- Se já recebeu o lote de dados com defeito, procure **qual registro quebra qual condição** e registre o item 4 com a **causa técnica** (ex.: valor `None`, texto vazio, número negativo, divisão por zero).
- No item 5, cite a fonte da decisão: livro (*Pense em Python*), documentação ou exercício que você resolveu.
- Compare com o **Campo 02**: o desvio de hoje já estava previsto no seu dimensionamento?
</details>

#### Registro do Ciclo 04 — 02/09

*Registro retrospectivo em 15/11/2026.*

1. **Desafio do ciclo (em 1 frase):** Usar condicionais para escolher uma operação no menu e aplicar a regra de que toda mídia cadastrada precisa ter título.
2. **O que implementei (commits / arquivos / links):** Usei `if` e `elif` para encaminhar a opção digitada à operação correspondente. No cadastro, o `if` bloqueia o título vazio e o `else` permite guardar a mídia quando o título passa nessa validação. A evidência está em [`crud_filmes_e_series.py` na branch `ciclo-1--terminal`](https://github.com/pedruck9-crypto/algoritmos-e-programacao/blob/ciclo-1--terminal/crud_filmes_e_series.py).
3. **Objeto(s) de conhecimento mobilizado(s):** Estruturas condicionais (`if`, `elif`, `else`), comparação de igualdade (`==`) e validação de entrada.
4. **Desvio ou erro encontrado + causa técnica:** Um título com apenas espaços é diferente de uma string vazia até que os espaços sejam removidos. Ao testar essa entrada, o programa exibiu “O título não pode ficar vazio.” e impediu o cadastro. Esse caso estava previsto no item 2c.
5. **Decisão de ajuste + fonte:** Usei `.strip()` antes de comparar o título com `""`. Assim, uma entrada formada só por espaços se torna vazia e aciona a validação. A [documentação do Python sobre `str.strip()`](https://docs.python.org/pt-br/3/builtins/stdtypes.html#str.strip) explica como a remoção de espaços funciona.
6. **Feedback recebido e o que mudei:** Não recebi feedback específico sobre as condicionais do meu CRUD nesta etapa.
7. **Próximo passo:** Testar uma opção fora do menu e verificar se o programa informa que a opção é inválida e mantém o menu aberto.

---

# 🟠 GRUPO 2 — prazo sábado 21/11 às 23h59

> **Janela:** segunda 16/11 → sábado 21/11. **O que entregar:** Registros dos Ciclos 05, 06, 07 e 08 · Checkpoint Conceitual · Campo 03 · Campo 04.
>
> ⚠️ O prazo cai num **sábado**: planeje terminar na sexta. Os campos do Ciclo 03 (Checkpoint, 03 e 04) aparecem **primeiro**, porque são a base da investigação.

**Checklist do Grupo 2**
- [ ] Checkpoint Conceitual feito conforme orientação do professor (20 min, sem consulta)
- [ ] Campo 03: 2 achados com objeto, 1 desvio com causa técnica, 1 decisão com fonte
- [ ] Campo 04: ferramenta, pergunta íntegra, resumo, o que aceitei e o que questionei
- [ ] Registros dos Ciclos 05, 06, 07 e 08 com os 7 itens (devolutiva da P1 no ciclo 06)
- [ ] Commits no GitHub e painel atualizado

## 🟠 CICLO 03 (campos) — 26/08 — Checkpoint, Campo 03 e Campo 04

<details>
<summary>📘 Orientações — Checkpoint, Campo 03 e Campo 04 (referentes ao Ciclo 03)</summary>

**Checkpoint Conceitual** · *20 min · sem consulta · conforme orientação do professor*
- Verifica o **seu domínio individual** do conteúdo — não avalia a sua solução. São **3 questões dissertativas**. Quem investiu por conta própria responde com segurança.
- Respostas **genéricas, sem ancoragem técnica, não são aceitas**. Defina o objeto **e** relacione-o ao problema do seu CRUD, explicitando as implicações.
- Critérios: *precisão conceitual*, *relação conteúdo-problema*, *qualidade do raciocínio*.
- Se for insatisfatório, você recebe **feedback escrito em até 48h** e deve ajustar a investigação antes da avaliação somativa.
- Se o professor aplicar o Checkpoint via GitHub, use o arquivo abaixo **só durante os 20 minutos**, com um único commit ao final.

**Campo 03 — Execução e desvios** · *sábado 21/11, 23h59*
- **3a.** Pelo menos **2 achados** que mudaram sua compreensão do problema, cada um com o **objeto de conhecimento** associado.
- **3b.** Pelo menos **1 desvio** em relação ao Campo 02 (o que você planejou e não aconteceu) e a **causa técnica** — não vale "falta de tempo".
- **3c.** Pelo menos **1 decisão de ajuste**, com justificativa e **fonte**, e o objeto de conhecimento mobilizado.

**Campo 04 — Interação com IA** · *sábado 21/11, 23h59 · obrigatório e avaliado*
- Registre **pelo menos uma** interação real com uma IA sobre o seu CRUD.
- **4b.** Transcreva a pergunta **na íntegra** (copie e cole).
- **4c.** Resuma a resposta em **um parágrafo** com as suas palavras.
- **4d.** O que você **aceitou**, ligando ao objeto de conhecimento.
- **4e.** O que você **questionou ou descartou**, com **argumento técnico ou fonte** (teste, documentação, livro). Dica: **rode o código** que a IA sugeriu antes de decidir.
- **Print sem análise crítica = devolução imediata.** Se você aceitou tudo, volte e procure o que verificar.
</details>

### 🧩 CHECKPOINT CONCEITUAL INDIVIDUAL
*20 minutos · sem consulta a qualquer fonte, material ou colega · conforme orientação do professor.*

**Pendência registrada em 21/11/2026:** recebi no grupo da turma o esclarecimento de que “3a = questão 1” se refere ao Campo 03. Ainda não recebi o enunciado das três questões nem a confirmação sobre a aplicação do checkpoint. Solicitei esclarecimento ao professor e aguardo orientação para realizá-lo em 20 minutos, sem consulta.

| | |
|---|---|
| **Nome do estudante** | _…_ |
| **Data de realização** | _…_ |
| **Unidade curricular** | Algoritmos e Programação |
| **Professor(a)** | Rondineli Seba Salomão |

> **INSTRUÇÕES:** Responda individualmente, sem consulta. Você tem 20 minutos. As questões avaliam seu domínio dos objetos de conhecimento do componente — não sua solução para o problema. Respostas genéricas sem ancoragem técnica não são aceitas.

**QUESTÃO 1** — Objeto de conhecimento: _…_
> _(Questão elaborada pelo professor na Proposta — Apêndice A, item 6)_

**RESPOSTA:**

> _…_

**QUESTÃO 2** — Objeto de conhecimento: _…_
> _(Questão elaborada pelo professor na Proposta — Apêndice A, item 6)_

**RESPOSTA:**

> _…_

**QUESTÃO 3** — Objeto de conhecimento: _…_
> _(Questão elaborada pelo professor na Proposta — Apêndice A, item 6)_

**RESPOSTA:**

> _…_

<details>
<summary>🔒 Uso do professor — critérios de avaliação do Checkpoint</summary>

| CRITÉRIO | SATISFATÓRIO | INSATISFATÓRIO |
|---|---|---|
| **Precisão conceitual** | Domínio do objeto de conhecimento, com vocabulário técnico adequado e sem erros conceituais relevantes. | Resposta vaga, com erros conceituais ou sem ancoragem nos objetos de conhecimento do componente. |
| **Relação conteúdo-problema** | Conecta o objeto de conhecimento ao problema trabalhado na AFP. | Responde o objeto de forma isolada, sem relação com o problema do ciclo. |
| **Qualidade do raciocínio** | Raciocínio técnico articulado: relaciona o objeto ao problema e explicita implicações para a investigação. | Apenas define o objeto, sem articular raciocínio ou relação com o problema investigado. |

**RESULTADO:** ☐ Satisfatório ☐ Insatisfatório
**AÇÃO DO PROFESSOR:** Checkpoint insatisfatório gera feedback escrito individualizado até 48h — o aluno ajusta a investigação antes da avaliação somativa.
</details>

### 🧩 CAMPO 03 — Execução e desvios
*AV Qualis — Grupo 2 | Sábado 21/11, 23h59*

**3a. O que descobri que mudou minha compreensão do problema (mínimo 2 achados, com objeto de conhecimento associado):**

*Rascunho para a defesa, registrado em 17/11/2026.*

1. **Validação de entrada e condicionais.** Testei o cadastro com um título formado apenas por espaços. O método .strip() transformou a entrada em uma string vazia, e a condição bloqueou o cadastro. Entendi que preciso verificar o texto depois de remover os espaços das pontas.
2. **Listas e persistência de dados.** Ao fechar e reabrir a versão de terminal, observei que o catálogo estava vazio. Entendi que append() acrescenta mídias à lista durante a execução. Ao reiniciar, o programa cria uma lista vazia porque essa versão guarda os registros apenas em memória.

**3b. Desvio em relação ao Campo 02 (ao menos 1 — causa técnica):**

- **Execução do planejamento:** executei os três testes previstos no Campo 02. Conferi a listagem de duas mídias, a rejeição de um título formado apenas por espaços e o catálogo após fechar e reabrir o programa. Os testes seguiram o planejamento.
- **Desvio anterior de escopo:** o professor havia permitido front-end, e criei uma interface web para o catálogo. Acrescentei FastAPI para disponibilizar operações por uma API, SQLite para persistir os cadastros e um ORM para acessar o banco. Esses recursos ampliaram o projeto além dos conteúdos previstos para a versão acadêmica.
- **Causa e ajuste:** minha interpretação inicial do escopo levou à adoção dessas tecnologias. Quando compreendi a delimitação, reorganizei o código em branches com versões de terminal para demonstrar variáveis, condicionais, laços, estruturas dinâmicas e funções. Mantive a versão web ampliada como evolução para o portfólio.
- **Pendência:** confirmar com o professor se esse desvio anterior pode atender ao item 3b, que pede um desvio em relação ao Campo 02.

**3c. Decisão de ajuste (ao menos 1) com justificativa e fonte:**

- **Decisão:** mantive .strip() antes da comparação do título com "". Assim, a entrada vazia ou formada apenas por espaços aciona a condição que bloqueia o cadastro. No teste, observei a mensagem de título obrigatório e a rejeição do cadastro.
- **Fonte:** [Documentação do Python sobre str.strip()](https://docs.python.org/pt-br/3/builtins/stdtypes.html#str.strip).

**Objeto de conhecimento mobilizado nesta decisão:** tratamento de strings, validação de entrada e estruturas condicionais.

### 🧩 CAMPO 04 — Interação com IA
*AV Qualis — Grupo 2 | Sábado 21/11, 23h59 | OBRIGATÓRIO*

> **Obrigatório e avaliado. Print sem análise crítica = devolução imediata. Reproduzir a IA sem questionamento = reprovado.**

**4a. Ferramenta:** Codex. **Data da interação original:** 16/11/2026.

*Rascunho para a defesa, registrado em 17/11/2026.*

**Ferramenta:** Codex. **Data da interação original:** 16/11/2026. **Data do registro:** 17/11/2026.

**4b. Pergunta formulada (transcrita integralmente):**

> no item 4 do ciclo 04 como poderia ficar o texto

**4c. Resposta da IA (resumida em parágrafo):**

> O Codex sugeriu registrar o teste com um título formado apenas por espaços. Explicou que .strip() transforma essa entrada em uma string vazia e que a condição do cadastro detecta esse valor e impede o registro. Também orientou a apresentar o resultado como observado depois de executar o teste.

**4d. O que aceitei — com referência ao objeto de conhecimento do componente:**

> Aceitei a sugestão de explicar a causa técnica junto com o resultado. Conferi que .strip() trata a entrada e que a estrutura condicional bloqueia o cadastro. Os conceitos envolvidos são tratamento de strings, validação de entrada e condicionais.

**4e. O que questionei ou descartei — com argumento técnico ou fonte:**

> Questionei se a explicação do Codex correspondia ao comportamento do meu CRUD. Conferi o código e testei um título formado apenas por espaços. O programa exibiu “O título não pode ficar vazio.” e impediu o cadastro. Por isso, aceitei a explicação após verificá-la. Nessa interação, não descartei nenhuma sugestão.

**Referência para a verificação:** [Documentação do Python sobre str.strip()](https://docs.python.org/pt-br/3/builtins/stdtypes.html#str.strip).

## 🟠 CICLO 05 — 09/09 — Condicionais aninhadas e operadores lógicos

<details>
<summary>📘 Orientações do Ciclo 05</summary>

- **Sem Campo do Protocolo hoje.** Preencha o Registro do Ciclo 05.
- Registre **qual combinação de condições** (`and`, `or`, `not`) você precisou e **por que** uma condicional aninhada ou um operador lógico foi a melhor escolha.
- Descreva **pelo menos um caso de teste** que você usou para provar a lógica (entrada → resultado esperado → resultado obtido).
- **Atenção à P1 (23/09):** reveja o Logbook até aqui. Complete itens em branco e confirme se os commits estão em dia.
- Na semana de 16/09 (Nivelamento / Peer Instruction), reserve 10 minutos para atualizar este arquivo.
</details>

#### Registro do Ciclo 05 — 09/09

*Registro retrospectivo em 21/11/2026.*

1. **Desafio do ciclo (em 1 frase):** Organizar as verificações do cadastro para impedir que uma nova mídia sobrescreva a existente ou seja cadastrada sem título.
2. **O que implementei (commits / arquivos / links):** Na primeira versão de terminal, coloquei verificações dentro da opção de cadastro. O programa verifica a variável cadastrada. Se já existe uma mídia, informa que é necessário excluí-la antes de cadastrar outra. Caso contrário, recebe o título e verifica se ele ficou vazio após .strip(). Evidência: [código da primeira versão](https://github.com/pedruck9-crypto/algoritmos-e-programacao/blob/ciclo-1--terminal/crud_filmes_e_series.py).
3. **Objeto(s) de conhecimento mobilizado(s):** Condicionais aninhadas, valores booleanos, comparação de igualdade e validação de entrada. Usei o aninhamento porque a verificação do título só precisa acontecer quando o usuário escolhe cadastrar e ainda não existe uma mídia.
4. **Desvio ou erro encontrado + causa técnica:** Testei cadastrar uma segunda mídia sem excluir a primeira. **Entrada:** opção 1 com cadastrada igual a True. **Resultado esperado:** bloquear o segundo cadastro e preservar o primeiro. **Resultado obtido:** o programa exibiu “Já existe uma mídia cadastrada. Exclua-a antes de cadastrar outra.” A verificação do estado do cadastro impediu a substituição dos dados.
5. **Decisão de ajuste + fonte:** Organizei as verificações em condicionais aninhadas para bloquear um novo cadastro antes de receber dados que substituiriam os existentes. Consultei [Instruções if](https://docs.python.org/pt-br/3/tutorial/controlflow.html#if-statements) para compreender o controle de execução.
6. **Feedback recebido e o que mudei:** Não recebi feedback específico nesta etapa.
7. **Próximo passo:** Testar o cadastro com o catálogo vazio e após excluir uma mídia.

## 🟠 CICLO 06 — 30/09 — Devolutiva da P1 + repetição: `for`, `while`, `break`, `continue`

<details>
<summary>📘 Orientações do Ciclo 06</summary>

- **Sem Campo do Protocolo hoje.** Preencha o Registro do Ciclo 06.
- Use o item 6 para registrar a **devolutiva da P1**: o que errou e **qual conceito** estava faltando. Esses erros alimentam o **Campo 07c** (conceitos corrigidos). *Anote já, para não esquecer.*
- Registre **por que escolheu `for` ou `while`** em cada laço do seu CRUD (cadastro em lote, listagem, menu).
- Item 4: se um laço ficou infinito ou pulou itens, descreva a **causa técnica** (condição de parada, incremento, `break` fora de lugar).
</details>

#### Registro do Ciclo 06 — 30/09

*Registro retrospectivo em 21/11/2026.*

1. **Desafio do ciclo (em 1 frase):** Manter o menu disponível para várias operações e encerrar o laço quando o usuário escolher sair.
2. **O que implementei (commits / arquivos / links):** Usei while True para repetir a exibição do menu e a leitura da opção. Depois de uma operação, o programa volta ao início do laço. Na opção de saída, usei break. Evidência: [código da primeira versão](https://github.com/pedruck9-crypto/algoritmos-e-programacao/blob/ciclo-1--terminal/crud_filmes_e_series.py).
3. **Objeto(s) de conhecimento mobilizado(s):** Laço while, condição booleana, interrupção com break e controle do fluxo de execução.
4. **Desvio ou erro encontrado + causa técnica:** **Entrada:** uma opção fora do menu. **Resultado esperado:** mensagem de opção inválida e reapresentação do menu. **Resultado obtido:** o programa exibiu “Opção inválida. Tente novamente.” e voltou a mostrar o menu. Não identifiquei erro nesse teste.
5. **Decisão de ajuste + fonte:** Mantive o menu e a leitura da opção dentro de while True para permitir novas operações. Usei break na opção de sair para encerrar esse laço. Fontes: [A instrução while](https://docs.python.org/pt-br/3/reference/compound_stmts.html#the-while-statement) e [break e continue](https://docs.python.org/pt-br/3/tutorial/controlflow.html#break-and-continue-statements).
6. **Feedback recebido (inclui devolutiva da P1) e o que mudei:** Até 21/11/2026, consultei o Classroom e o sistema acadêmico e encontrei apenas a nota da P1. Ainda não localizei a prova corrigida ou comentários que permitam identificar meus erros. Solicitei orientação ao professor e aguardo resposta para registrar a devolutiva e o que preciso revisar.
7. **Próximo passo:** Testar uma sequência de cadastro, consulta e saída na mesma execução para conferir a repetição e o encerramento do menu.

## 🟠 CICLO 07 — 07/10 — Listas: armazenamento e iteração

<details>
<summary>📘 Orientações do Ciclo 07</summary>

- **Sem Campo do Protocolo hoje.** Preencha o Registro do Ciclo 07.
- Justifique **por que seus dados cabem em uma lista** e como você os percorre (iteração).
- Item 4: erros típicos — índice fora do intervalo, alterar a lista enquanto percorre, confundir cópia com referência. Registre qual deles aconteceu e a causa técnica.
- Item 3: nomeie as **operações de lista** que usou (adicionar, remover, ordenar, fatiar…).
</details>

#### Registro do Ciclo 07 — 07/10

*Registro retrospectivo em 21/11/2026.*

1. **Desafio do ciclo (em 1 frase):** Armazenar vários elementos em uma lista e percorrê-los para exibir seus valores no terminal.
2. **O que implementei (commits / arquivos / links):** No laboratório, trabalhei com lista_jogos. Usei for com enumerate() para obter o índice e o nome de cada jogo, fatiamento para selecionar parte da lista e append() para adicionar um item. No CRUD, midias.append(midia) acrescenta um cadastro ao catálogo. Evidência: [exercício da lista de jogos](AULAS/lista_jogos.py).
3. **Objeto(s) de conhecimento mobilizado(s):** Listas, índices, iteração com for, enumerate(), fatiamento e inclusão com append(). A lista reúne os elementos e o laço percorre os itens.
4. **Desvio ou erro encontrado + causa técnica:** Na primeira versão do exercício, print() mostrava apenas o nome do jogo. O índice era obtido por enumerate(), mas não era passado à função de saída. Ajustei para print(indice, jogo) e observei os dois valores na mesma linha ao executar a versão corrigida.
5. **Decisão de ajuste + fonte:** Usei enumerate() para obter a posição e o valor de cada elemento durante a repetição. Isso facilitou a identificação dos itens na saída. A fonte foi a orientação recebida na aula prática do laboratório.
6. **Feedback recebido e o que mudei:** No laboratório, recebi orientação para usar # ao escrever comentários e para exibir o índice junto com o nome do jogo. Acrescentei comentários e ajustei o comando para print(indice, jogo).
7. **Próximo passo:** Cadastrar duas mídias, listar os registros e excluir a primeira. Depois, conferir a posição da segunda na lista e seu ID.

## 🟠 CICLO 08 — 14/10 — Busca/consulta e introdução a dicionários e matrizes

<details>
<summary>📘 Orientações do Ciclo 08</summary>

- **Sem Campo do Protocolo hoje.** Preencha o Registro do Ciclo 08.
- Explique **por que cada item do seu catálogo virou um dicionário** (chave → valor) em vez de uma lista de valores soltos.
- Item 4: registre **qual busca falhou** (item inexistente, tipo diferente — `"2"` ≠ `2`, chave com maiúscula errada) e a causa técnica.
- Se usou o lote de dados defeituoso, registre **qual registro** quebrou a busca.
- Item 5: cite a fonte (*Pense em Python*, cap. 11, ou outra).
</details>

#### Registro do Ciclo 08 — 14/10

*Registro retrospectivo em 21/11/2026.*

1. **Desafio do ciclo (em 1 frase):** Localizar uma mídia pelo identificador e consultar os dados desse cadastro.
2. **O que implementei (commits / arquivos / links):** Organizei cada mídia em um dicionário com as chaves id, titulo, tipo, genero, ano e sinopse. Os dicionários ficam na lista midias. A consulta percorre a lista e compara o ID de cada mídia com o identificador informado. Evidência: [versão com estruturas dinâmicas](https://github.com/pedruck9-crypto/algoritmos-e-programacao/tree/ciclo-2-estruturas-din%C3%A2micas).
3. **Objeto(s) de conhecimento mobilizado(s):** Dicionários, pares de chave e valor, lista de dicionários, iteração com for, comparação de igualdade e busca sequencial.
4. **Desvio ou erro encontrado + causa técnica:** Não identifiquei erro nos testes de busca realizados. **Teste 1:** informei ID 2, correspondente ao filme Interestelar. Esperava seus dados e o terminal exibiu título, tipo, gênero, ano e sinopse. **Teste 2:** informei ID 99, que não estava cadastrado. Esperava a indicação de ausência e o terminal exibiu “Mídia não encontrada.”
5. **Decisão de ajuste + fonte:** Usei dicionários para acessar os campos pelos nomes das chaves, como midia["id"] e midia["titulo"]. Na busca, comparo o identificador informado com a chave id de cada registro. Consultei [Dicionários](https://docs.python.org/pt-br/3/tutorial/datastructures.html#dictionaries) para compreender pares de chave e valor e acesso aos campos.
6. **Feedback recebido e o que mudei:** Não recebi feedback específico nesta etapa.
7. **Próximo passo:** Testar a busca com o catálogo vazio.

---

# 🔵 GRUPO 3 — prazo quinta 26/11 às 23h59

> **Janela:** sábado 21/11 → quinta 26/11. **O que entregar:** Registros dos Ciclos 09, 10, 11 e 12 · Campo 05 (duas revisões por pares) · Campo 06 · Campo 07.
>
> ⚠️ O prazo vem **um dia depois da P2 (25/11)**. Os Campos 06 e 07 dependem de todo o Logbook: deixe-os para o final, mas **adiante o rascunho do 6c e do 7a/7b antes da Defesa (18/11)**.

**Checklist do Grupo 3**
- [ ] Registros dos Ciclos 09, 10, 11 e 12 com os 7 itens
- [ ] Campo 05: duas revisões (Ciclos 09 e 12), blocos 5a a 5e
- [ ] Campo 06: decisão autônoma, lacuna com plano, pergunta da banca com 5 linhas ou mais
- [ ] Campo 07: 7a a 7e, com 3 objetos, 2 equívocos corrigidos e transferência
- [ ] Coerência entre Campo 01 e Campo 07
- [ ] Painel de acompanhamento completo

## 🔵 CICLO 09 — 21/10 — Atualização e exclusão: CRUD completo

<details>
<summary>📘 Orientações do Ciclo 09 — Registro + Campo 05 (revisão por pares nº 1)</summary>

- Neste ciclo seu CRUD ficou **completo** (Create, Read, Update, Delete). Preencha o Registro do Ciclo 09.
- **Item 4:** *atualizar* ou *excluir* item inexistente, e excluir durante um laço (a lista muda de tamanho e itens são pulados) são erros comuns.
- **Campo 05 — Registro de Revisão por Pares.** Você passa a ser **revisor** do CRUD de um colega.
  - Cada revisão tem **um registro** (copie a seção do Campo 05) com o nome e o link do repositório revisado.
  - **Revise o processo, não só o código:** o que foi decidido, em que objeto de conhecimento se apoia, com que fonte.
  - **5a:** liste as etapas da revisão (ex.: rodar o CRUD, testar com o lote de dados com defeito, ler o código, registrar achados, devolver feedback).
  - **5b:** liste os insumos que usou (lote de dados, casos de teste, `requisitos.md`) com quantidade planejada, utilizada e variação.
  - **5c:** diga se a solução do colega atende ao critério (Sim/Parcialmente/Não) e **qual critério** usou (ex.: requisito do `requisitos.md`).
  - **5d:** riscos da revisão (ex.: não conseguir rodar o código do colega) e como mitigou.
  - **5e:** registre **cada decisão técnica** da revisão com **data, responsável, objeto de conhecimento e fundamentação/referência**. *Sem objeto e sem referência, não é rastreável.*
  - Feedback ao colega: **específico e respeitoso** (o que está bom, o que quebrou, como reproduzir, sugestão).
</details>

#### Registro do Ciclo 09 — 21/10
1. **Desafio do ciclo (em 1 frase):** _…_
2. **O que implementei (commits / arquivos / links):** _…_
3. **Objeto(s) de conhecimento mobilizado(s):** _…_
4. **Desvio ou erro encontrado + causa técnica:** _…_
5. **Decisão de ajuste + fonte:** _…_
6. **Feedback recebido e o que mudei:** _…_
7. **Próximo passo:** _…_

### 🧩 CAMPO 05 — Registro de Revisão por Pares
*Adaptação do **Logbook do Time** (Apêndice C) para o CRUD individual. Documento atualizado pelo **revisor**. Cada decisão técnica relevante deve ter associado o objeto de conhecimento correspondente.*

> ⚠️ **Nota de adaptação:** o Apêndice C original prevê Gestor, Responsável Técnico, Analista de Qualidade e Comunicador. Como o CRUD é **individual** e os alunos atuam como **revisores**, mantive os blocos 5a a 5e e troquei os papéis por **Autor** (dono do CRUD) e **Revisor** (você). *Pendente de validação do professor/NDE.*

> **O Logbook de revisão é um registro de conhecimento em ação.** Cada decisão técnica relevante deve estar associada ao objeto de conhecimento que a fundamenta, à justificativa técnica e à referência utilizada. Registros sem esse vínculo não são aceitos.

#### Revisão nº 1

| | |
|---|---|
| **Autor do CRUD revisado** | _nome_ |
| **Repositório revisado** | _link_ |
| **Revisor** | _seu nome_ |
| **Unidade curricular / Semestre** | Algoritmos e Programação · 2026.2 |
| **Ciclo / data** | _Ciclo 09 · 21/10_ |

**5a. AVANÇO DO PROCESSO DE REVISÃO — análise técnica de cada etapa:**

| ETAPA DO PROCESSO | RESPONSÁVEL | PRAZO | STATUS | DESVIO / JUSTIFICATIVA |
|---|---|---|---|---|
| 1. _…_ | Revisor / Autor | _DD/MM_ | ☐ Concluída ☐ Em andamento ☐ Com desvio | _…_ |
| 2. _…_ | Revisor / Autor | _DD/MM_ | ☐ Concluída ☐ Em andamento ☐ Com desvio | _…_ |
| 3. _…_ | Revisor / Autor | _DD/MM_ | ☐ Concluída ☐ Em andamento ☐ Com desvio | _…_ |
| 4. _…_ | Revisor / Autor | _DD/MM_ | ☐ Concluída ☐ Em andamento ☐ Com desvio | _…_ |
| 5. _…_ | Revisor / Autor | _DD/MM_ | ☐ Concluída ☐ Em andamento ☐ Com desvio | _…_ |

**5b. ANÁLISE DE INSUMOS E CRITÉRIOS DE QUALIDADE:**

| RECURSO | QTDE PLANEJADA | QTDE UTILIZADA | VARIAÇÃO | JUSTIFICATIVA TÉCNICA |
|---|---|---|---|---|
| _…_ | _…_ | _…_ | _…_ | _…_ |
| _…_ | _…_ | _…_ | _…_ | _…_ |
| _…_ | _…_ | _…_ | _…_ | _…_ |

**5c. CONTROLE DE QUALIDADE:**
- **Critério ou norma técnica:** _…_
- **A solução atende?** ☐ Sim ☐ Parcialmente ☐ Não

**5d. GESTÃO DE RISCOS:**
- **Risco:** _…_
- **Estratégia de mitigação:** _…_

**5e. RASTREABILIDADE DAS DECISÕES TÉCNICAS — COM VÍNCULO AO CONTEÚDO:**

| DATA | DECISÃO TÉCNICA | RESP. | OBJETO DE CONHECIMENTO MOBILIZADO | FUNDAMENTAÇÃO / REFERÊNCIA |
|---|---|---|---|---|
| _DD/MM/AA_ | _…_ | _…_ | _…_ | _…_ |
| _DD/MM/AA_ | _…_ | _…_ | _…_ | _…_ |
| _DD/MM/AA_ | _…_ | _…_ | _…_ | _…_ |
| _DD/MM/AA_ | _…_ | _…_ | _…_ | _…_ |
| _DD/MM/AA_ | _…_ | _…_ | _…_ | _…_ |

> **IMPORTANTE:** Decisão registrada sem objeto de conhecimento associado e sem referência é considerada **não rastreável** e não conta para a avaliação formativa. O vínculo entre processo e conteúdo é obrigatório em todas as decisões relevantes.

## 🔵 CICLO 10 — 28/10 — Modularização: funções

<details>
<summary>📘 Orientações do Ciclo 10</summary>

- **Sem Campo do Protocolo hoje.** Preencha o Registro do Ciclo 10.
- Explique **como dividiu** o CRUD em funções (`cadastrar()`, `buscar()`, `alterar()`, `excluir()`, `listar()`, `menu()`) e **por que** cada função tem aquela responsabilidade.
- Item 4: erros típicos — variável fora de escopo, função sem `return`, parâmetro na ordem errada.
- Compare o código **antes e depois** da refatoração: o que ficou mais claro? Registre no item 6 o feedback do colega que fez a *peer review*.
</details>

#### Registro do Ciclo 10 — 28/10
1. **Desafio do ciclo (em 1 frase):** _…_
2. **O que implementei (commits / arquivos / links):** _…_
3. **Objeto(s) de conhecimento mobilizado(s):** _…_
4. **Desvio ou erro encontrado + causa técnica:** _…_
5. **Decisão de ajuste + fonte:** _…_
6. **Feedback recebido e o que mudei:** _…_
7. **Próximo passo:** _…_

## 🔵 CICLO 11 — 04/11 — Recursividade

<details>
<summary>📘 Orientações do Ciclo 11 — Registro + Campo 06 (Grupo 3)</summary>

- Preencha o Registro do Ciclo 11 (caso base, chamada recursiva, pilha de execução).
- **Campo 06 — Próximos passos para a defesa** · *individual · quinta 26/11, 23h59*. Prepare-se para a **Defesa Técnica de quarta 18/11**: como o prazo é posterior à defesa, **adiante pelo menos o 6c** (pergunta da banca e resposta) e leve-o para a arguição.
  - **6a.** Uma **decisão técnica que você defende com plena autonomia**: algo que aprendeu e **é exclusivamente seu**, que nenhum colega consegue explicar por você.
  - **6b.** Uma **lacuna técnica real** e um **plano de ação** com passos e datas para saná-la antes da defesa.
  - **6c.** Uma **pergunta que a banca pode fazer** (nível de Avaliação ou Criação) e a sua **resposta fundamentada em, no mínimo, 5 linhas**, com o objeto de conhecimento e a fonte.
  - Dica: leia a **Rubrica de Defesa Técnica** (no Encerramento) e escolha uma pergunta que teste *aplicação*, *evolução* ou *transferência*.
</details>

#### Registro do Ciclo 11 — 04/11
1. **Desafio do ciclo (em 1 frase):** _…_
2. **O que implementei (commits / arquivos / links):** _…_
3. **Objeto(s) de conhecimento mobilizado(s):** _…_
4. **Desvio ou erro encontrado + causa técnica:** _…_
5. **Decisão de ajuste + fonte:** _…_
6. **Feedback recebido e o que mudei:** _…_
7. **Próximo passo:** _…_

### 🧩 CAMPO 06 — Próximos passos para a defesa
*AV Qualis — Grupo 3 | Individual | Quinta 26/11, 23h59*

**6a. Decisão técnica que defendo com plena autonomia — o que aprendi que é exclusivamente meu e não consigo transferir para nenhum colega:**

> _…_

**6b. Lacuna técnica e plano de ação para saná-la:**

- **Lacuna:** _…_
- **Plano de ação (passos e datas):** _…_

**6c. Pergunta que a banca pode fazer — com resposta fundamentada (mínimo 5 linhas):**

*Rascunho para a defesa, registrado em 17/11/2026.*

- **Pergunta:** por que os filmes e séries somem ao fechar o CRUD de terminal e como você adaptaria essa versão para recuperar os cadastros na próxima execução?
- **Resposta:**

> Na versão de terminal que testei, os cadastros ficam na lista midias, que começa vazia quando o programa é iniciado.
>
> Cada cadastro usa midias.append(midia) para acrescentar um registro à lista em memória.
>
> Ao fechar e reabrir o programa, observei que o catálogo estava vazio, pois essa versão não grava os registros em um arquivo.
>
> Se a persistência fizesse parte do escopo, eu usaria json.dump() para gravar a lista após cadastrar, atualizar ou excluir e json.load() para recuperá-la ao iniciar.
>
> Na primeira execução, se o arquivo ainda não existisse, o catálogo começaria vazio.
>
> Para verificar a solução, eu cadastraria duas mídias, fecharia o programa e conferiria se os dois registros aparecem depois de reabri-lo.

**Objeto de conhecimento mobilizado:** listas, armazenamento em memória, leitura e escrita de arquivos e persistência de dados.

**Fonte:** [Tutorial do Python sobre JSON](https://docs.python.org/pt-br/3/tutorial/inputoutput.html#saving-structured-data-with-json).

## 🔵 CICLO 12 — 11/11 — Refatoração e qualidade de código

<details>
<summary>📘 Orientações do Ciclo 12 — Registro + Campo 05 (revisão nº 2) + início do Campo 07</summary>

- Preencha o Registro do Ciclo 12. Registre o que revisou: código duplicado, nomes ruins, funções grandes, comentários desnecessários, lógica confusa.
- **Campo 05 — Revisão por pares nº 2.** Foque em **qualidade**: o CRUD do colega resiste aos casos de teste (mínimos, máximos, inválidos, entradas vazias) e ao **lote de dados com defeito**? Use a seção abaixo (copie o bloco *Revisão nº 1* do Ciclo 09 e preencha novamente).
- **Campo 07 — Evolução conceitual** · *individual · quinta 26/11, 23h59.* Comece agora, enquanto a memória do semestre está fresca; leve o rascunho de 7a e 7b para a Defesa de 18/11. Dicas por item:
  - **7a.** Releia o **Campo 01** e resuma o que você *pensava* e *achava que sabia*. Seja honesto, mesmo se o Campo 01 estiver "errado".
  - **7b.** Pelo menos **3 objetos de conhecimento** na tabela: o que você *não dominava*, o que *aprendeu e consegue demonstrar* e a **evidência** (em qual Campo ou ciclo do Logbook aparece).
  - **7c.** Pelo menos **2 equívocos corrigidos**, dizendo **o que os corrigiu** (Fechamento Teórico, pesquisa, *Peer Review*, arguição, devolutiva da P1).
  - **7d.** **Transferência:** um exemplo concreto de aplicar o que aprendeu em um **contexto diferente** do CRUD (outra área do seu curso ou outro tipo de sistema).
  - **7e.** Avaliação honesta do que **ainda não domina** e vai aprofundar.
</details>

#### Registro do Ciclo 12 — 11/11
1. **Desafio do ciclo (em 1 frase):** _…_
2. **O que implementei (commits / arquivos / links):** _…_
3. **Objeto(s) de conhecimento mobilizado(s):** _…_
4. **Desvio ou erro encontrado + causa técnica:** _…_
5. **Decisão de ajuste + fonte:** _…_
6. **Feedback recebido e o que mudei:** _…_
7. **Próximo passo:** _…_

### 🧩 CAMPO 05 — Registro de Revisão por Pares (revisão nº 2)

| | |
|---|---|
| **Autor do CRUD revisado** | _nome_ |
| **Repositório revisado** | _link_ |
| **Revisor** | _seu nome_ |
| **Ciclo / data** | _Ciclo 12 · 11/11_ |

**5a. AVANÇO DO PROCESSO DE REVISÃO:**

| ETAPA DO PROCESSO | RESPONSÁVEL | PRAZO | STATUS | DESVIO / JUSTIFICATIVA |
|---|---|---|---|---|
| 1. _…_ | Revisor / Autor | _DD/MM_ | ☐ Concluída ☐ Em andamento ☐ Com desvio | _…_ |
| 2. _…_ | Revisor / Autor | _DD/MM_ | ☐ Concluída ☐ Em andamento ☐ Com desvio | _…_ |
| 3. _…_ | Revisor / Autor | _DD/MM_ | ☐ Concluída ☐ Em andamento ☐ Com desvio | _…_ |
| 4. _…_ | Revisor / Autor | _DD/MM_ | ☐ Concluída ☐ Em andamento ☐ Com desvio | _…_ |
| 5. _…_ | Revisor / Autor | _DD/MM_ | ☐ Concluída ☐ Em andamento ☐ Com desvio | _…_ |

**5b. ANÁLISE DE INSUMOS E CRITÉRIOS DE QUALIDADE:**

| RECURSO | QTDE PLANEJADA | QTDE UTILIZADA | VARIAÇÃO | JUSTIFICATIVA TÉCNICA |
|---|---|---|---|---|
| _…_ | _…_ | _…_ | _…_ | _…_ |
| _…_ | _…_ | _…_ | _…_ | _…_ |
| _…_ | _…_ | _…_ | _…_ | _…_ |

**5c. CONTROLE DE QUALIDADE:**
- **Critério ou norma técnica:** _…_
- **A solução atende?** ☐ Sim ☐ Parcialmente ☐ Não

**5d. GESTÃO DE RISCOS:**
- **Risco:** _…_
- **Estratégia de mitigação:** _…_

**5e. RASTREABILIDADE DAS DECISÕES TÉCNICAS — COM VÍNCULO AO CONTEÚDO:**

| DATA | DECISÃO TÉCNICA | RESP. | OBJETO DE CONHECIMENTO MOBILIZADO | FUNDAMENTAÇÃO / REFERÊNCIA |
|---|---|---|---|---|
| _DD/MM/AA_ | _…_ | _…_ | _…_ | _…_ |
| _DD/MM/AA_ | _…_ | _…_ | _…_ | _…_ |
| _DD/MM/AA_ | _…_ | _…_ | _…_ | _…_ |
| _DD/MM/AA_ | _…_ | _…_ | _…_ | _…_ |
| _DD/MM/AA_ | _…_ | _…_ | _…_ | _…_ |

### 🧩 CAMPO 07 — Evolução conceitual
*AV Qualis — Grupo 3 | Individual | Quinta 26/11, 23h59*

*Evidência rastreável de aprendizagem entre o início e o encerramento do ciclo AFP.*

**7a. O que eu pensava no início do ciclo (com base no Campo 01 — registrar a hipótese inicial e os objetos de conhecimento que achava conhecer):**

*Rascunho para a defesa, registrado em 17/11/2026.*

> No início, meu conhecimento de Python era básico. Eu tinha dúvidas sobre como usar condicionais para tratar uma opção inválida no menu, por que os dados da lista desapareciam ao fechar o programa e como evitar mídias duplicadas. Minha hipótese inicial era que uma opção inválida pudesse seguir o mesmo caminho da opção 0 e acionar o break, encerrando o menu antes da hora.

**7b. O que aprendi — conceitos, princípios ou relações técnicas que não dominava no início e que agora consigo explicar com precisão (mínimo 3 objetos de conhecimento):**

| OBJETO DE CONHECIMENTO | O QUE EU NÃO DOMINAVA | O QUE APRENDI E CONSIGO DEMONSTRAR | EVIDÊNCIA (campo do Logbook onde aparece) |
|---|---|---|---|
| Condicionais e comparação de igualdade | Como o menu decide qual operação executar a partir da entrada. | Consigo explicar que input() devolve texto e que opcao == "1" verifica se o usuário escolheu o cadastro. | Registro do Ciclo 03, trecho do menu da versão de terminal. |
| Validação de entrada | Como uma condição aplica a regra de título obrigatório. | Consigo mostrar que .strip() transforma uma entrada só com espaços em "" e que a condição impede o cadastro. | Registro do Ciclo 04 e Campo 03a, teste do título com espaços. |
| Listas e persistência de dados | Por que as mídias desaparecem quando fecho o programa. | Consigo explicar que append() acrescenta registros à lista em memória e que a versão de terminal testada inicia um catálogo vazio ao reabrir. Estudei JSON como possibilidade de persistência. | Campo 02, itens 2a e 2b, e teste de reabertura no Campo 03a. |

**7c. Conceitos que precisei corrigir ao longo do ciclo — onde eu estava equivocado e o que o corrigiu (Fechamento Teórico, pesquisa, Peer Review, arguição):**

*Registro em 21/11/2026.*

1. **Equívoco:** eu confundia estruturas condicionais com laços de repetição e usava a expressão “laços de condicionais”.
   **Correção:** entendi que if, elif e else escolhem qual bloco executar, enquanto for e while repetem instruções.
   **O que corrigiu:** a revisão dos termos durante a elaboração do Logbook com apoio da IA e a análise do menu do meu CRUD.
2. **Equívoco:** eu dizia que a ausência de # impedia o programa de funcionar.
   **Correção:** entendi que o programa pode funcionar sem comentários. O # é necessário quando quero escrever uma observação no código para que o Python a ignore.
   **O que corrigiu:** a orientação recebida no laboratório sobre comentários e o esclarecimento dessa diferença durante a revisão do Logbook com apoio da IA.

**7d. Transferência — como este aprendizado se aplica a um contexto diferente do problema trabalhado (ao menos 1 exemplo concreto da área de formação):**

Eu poderia aplicar esses conceitos a um sistema de controle de estoque. Cada produto poderia ser representado por um dicionário com identificador, nome e quantidade, e uma lista reuniria os produtos. Usaria uma condição para impedir o cadastro de um produto com nome vazio e um laço para consultar os registros. Assim como no catálogo de mídias, precisaria distinguir a posição do produto na lista do identificador do cadastro.

**7e. Avaliação honesta do próprio percurso — o que ainda não domino e preciso aprofundar após este ciclo:**

Hoje consigo explicar melhor o funcionamento do menu, a validação de títulos e o armazenamento dos registros em uma lista. Ainda preciso aprofundar como salvar e recuperar dados entre execuções e como validar o conteúdo carregado de um arquivo. Também quero estudar uma regra para evitar mídias duplicadas, definindo quais dados devem ser comparados para identificar um cadastro repetido.

Pretendo aprofundar meus conhecimentos em front-end, área pela qual descobri afinidade durante o projeto. Após a defesa, também reconheci a necessidade de praticar a sintaxe de Python, incluindo dois-pontos, aspas, indentação e a distinção entre maiúsculas e minúsculas.

---

# 🏁 DEFESA TÉCNICA — quarta 18/11

<details>
<summary>📘 Orientações para a Defesa Técnica e preparação</summary>

**A Defesa é antes dos prazos dos Grupos 2 e 3.** Você será arguido sobre o que já estiver registrado e commitado. Priorize, até **terça 17/11**:
- [ ] **Grupo 1 entregue** (prazo 16/11): Identificação, Registros 01 a 04, Campos 01 e 02.
- [ ] **Campo 04 (IA)** e **Campo 03** ao menos em rascunho, para sustentar as perguntas sobre decisões (critérios 2 e 5).
- [ ] **Campo 06c** (pergunta da banca e resposta) e **rascunho de 7a e 7b**, para sustentar a evolução conceitual (critério 3).
- [ ] Registros dos Ciclos já feitos, mesmo que ainda não "entregues" no prazo do grupo.
- [ ] `README.md`, `docs/` e CRUD rodando.
- [ ] Você consegue explicar **cada linha** do seu código e **cada decisão** registrada.
- Os demais itens seguem com os prazos dos grupos (21/11 e 26/11). A banca pode consultar o histórico do Git.

**A Defesa Técnica é individual.** Você será arguido sobre o que registrou. Cada aluno recebe pelo menos **1 questão** nos níveis de **Avaliação** ou **Criação** (taxonomia de Bloom).

**Como a Rubrica se liga ao seu Logbook:**

| Critério da Rubrica | Onde você prepara a evidência |
|---|---|
| 1. Domínio dos objetos de conhecimento | Campos 01, 02 e 07b |
| 2. Aplicação do conteúdo à solução ⚠️ *inegociável* | Registros dos ciclos (itens 3 e 5), Campo 03c e Campo 05e |
| 3. Evolução conceitual ⚠️ *inegociável* | Campo 01 → Campo 07 (7a, 7b e 7c; leve o rascunho) |
| 4. Capacidade de transferência | Campo 07d |
| 5. Argumentação sob pressão | Campo 06c e Campo 04e |
| 6. Autonomia intelectual e coerência com o Logbook | Todo o Logbook (principalmente Campos 04 e 06a) |

**Treino:** peça a um colega que faça 3 perguntas "imprevistas" sobre o seu CRUD e responda **sem consultar** o Logbook. Se não conseguir, volte ao Campo 06b.
</details>

## 🧩 RUBRICA DE DEFESA TÉCNICA (revisada)
*Avaliação individual de cada membro na Semana 16. Cada membro recebe ao menos 1 questão nos níveis de Avaliação ou Criação da Taxonomia de Bloom. Critérios revisados para medir aprendizagem, aplicação, evolução e transferência do conteúdo.*

| | |
|---|---|
| **Nome** | Pedro Lucas Pereira Rolim |
| **Curso / Time / Função** | Sistemas de Informação, 2º período / Projeto individual / Autor do CRUD de filmes e séries |

<details>
<summary>🔒 Uso do professor — rubrica completa</summary>

| CRITÉRIO | EXCELENTE (4,0) | SATISFATÓRIO (3,0) | INSATISFATÓRIO (2,0) | AUSENTE (0) |
|---|---|---|---|---|
| **1. DOMÍNIO DOS OBJETOS DE CONHECIMENTO** — Responde com precisão técnica, sem apoio dos colegas, demonstrando aprendizagem do conteúdo. | Responde com precisão e profundidade, nomeando os objetos de conhecimento mobilizados sem hesitação. | Responde com precisão, com imprecisões pontuais que não comprometem o raciocínio. | Responde de forma vaga, com erros conceituais relevantes ou dependendo dos colegas. | Não responde ou demonstra desconhecimento total. |
| **2. APLICAÇÃO DO CONTEÚDO À SOLUÇÃO** — Demonstra como os objetos de conhecimento fundamentaram as decisões do processo. | Explicita com precisão qual objeto de conhecimento fundamentou cada decisão relevante do processo investigativo, citando referência e demonstrando por que aquele conhecimento era o mais adequado. | Estabelece a relação conteúdo-decisão na maioria das perguntas, com alguma imprecisão pontual. | Não consegue explicitar a relação entre o conteúdo e as decisões do processo investigativo com clareza. | Não demonstra nenhuma relação entre os objetos de conhecimento e as decisões tomadas. |
| **3. EVOLUÇÃO CONCEITUAL** — Demonstra aprendizagem em relação ao que sabia no início do ciclo. | Identifica com precisão o que aprendeu, o que corrigiu e como o conhecimento evoluiu ao longo do ciclo. | Demonstra evolução em parte dos conceitos trabalhados, com alguma dificuldade de articular a trajetória. | Dificuldade em identificar diferenças entre o que sabia no início e o que domina agora. | Não demonstra nenhuma percepção de evolução conceitual ao longo do ciclo. |
| **4. CAPACIDADE DE TRANSFERÊNCIA** — Aplica o conhecimento a um contexto diferente do problema trabalhado. | Consegue transferir o aprendizado para um contexto novo com fundamentação técnica precisa. | Realiza a transferência com imprecisões que não comprometem a lógica do raciocínio. | Demonstra dificuldade em aplicar o conhecimento a contextos diferentes do problema original. | Não consegue realizar nenhuma transferência do conhecimento para contexto diferente. |
| **5. ARGUMENTAÇÃO SOB PRESSÃO** — Mantém coerência técnica diante de questionamentos imprevistos. | Mantém raciocínio coerente, reconhece limites com honestidade e reformula com fundamentação. | Mantém coerência na maior parte, com hesitações pontuais sem perda do fio técnico. | Fragilidade técnica diante de questionamentos imprevistos. | Não sustenta argumentação técnica diante de nenhum questionamento. |
| **6. AUTONOMIA INTELECTUAL E COERÊNCIA COM O LOGBOOK** — Defende o que registrou com consciência e sem depender do grupo. | Defende com precisão as decisões do Logbook, demonstrando autoria plena e independência intelectual. | Defende a maioria das decisões com coerência, com alguma imprecisão ou apoio pontual. | Depende dos colegas ou demonstra desconhecimento de parte do que registrou no próprio Logbook. | Não reconhece o que registrou ou não demonstra autonomia intelectual durante a arguição. |

**PONTUAÇÃO:** _____ / 24,0 **CONCEITO:** _____________

**Conversão:** 20–24 = Excelente (4,0) | 14–19 = Satisfatório (3,0) | 8–13 = Insatisfatório (2,0) | < 8 = Ausente (0)

> ⚠️ **Critérios 2 (Aplicação) e 3 (Evolução Conceitual) são inegociáveis — AUSENTE em qualquer um deles implica nota máxima de 2,0 na Defesa, independentemente do desempenho nos demais.**

**OBSERVAÇÕES:** _…_

**Professor(a):** _________________  **Data:** ___________
</details>

### Registro do Encerramento — 18/11

*Registro retrospectivo em 21/11/2026, referente à defesa de 18/11/2026.*

1. **O que apresentei/defendi (em 1 frase):** Apresentei os seis slides sobre meu CRUD de filmes e séries, explicando a evolução das versões acadêmicas, os testes realizados, o uso da IA e uma proposta de persistência com JSON.
2. **Objeto(s) de conhecimento que a banca mais explorou:** O professor perguntou sobre FastAPI, SQLite e ORM, que mencionei como recursos além do escopo acadêmico, e se essas tecnologias estavam presentes no meu repositório do GitHub. A pergunta abordou a relação entre a arquitetura apresentada, o código disponível e a delimitação do projeto.
3. **Pergunta que mais me desafiou e como respondi:** O professor perguntou se FastAPI, SQLite e o ORM realmente estavam no meu GitHub. Respondi que sim, essas tecnologias estavam no repositório. Após a defesa, identifiquei que preciso aprofundar meu domínio da sintaxe de Python, especialmente o uso de dois-pontos, aspas, indentação e a distinção entre letras maiúsculas e minúsculas.
4. **O que levo deste semestre para o próximo módulo:** Aprendi a revisar o código com atenção à sintaxe e a registrar minhas ideias e decisões. Também compreendi a importância de documentar o projeto durante seu desenvolvimento, escolher uma licença para o código e apresentar a documentação de forma acessível a quem consulta meu portfólio.

   A experiência de adequar o CRUD ao escopo acadêmico me ensinou a avaliar quais partes do código podem ser reaproveitadas quando os requisitos são esclarecidos ou alterados. Percebi que orientações claras, objetivas e disponíveis nos canais adequados ajudam a evitar dúvidas e retrabalho.

   Descobri interesse pelo front-end e quero aprofundar meus conhecimentos nessa área. Pretendo continuar estudando Python, praticar a leitura das mensagens de erro e melhorar minha capacidade de explicar as decisões do código.

---

# 🆘 Estou atrasado no Logbook. E agora?

1. **Não apague nem "retroescreva" o passado.** Preencha agora e **escreva a data real** do preenchimento (ex.: *"preenchido com atraso em 12/11"*).
2. **Campo 01 e Checkpoint (sem consulta):** se perdeu a janela, registre **o que sabe hoje, sem consultar nada**, marcando-o como *preenchimento tardio*. Combine o tratamento com o professor.
3. **Priorize a ordem dos grupos:** Grupo 1 (16/11) → Defesa (18/11) → Grupo 2 (21/11) → Grupo 3 (26/11). Dentro de cada grupo, os Campos vêm antes dos Registros.
4. **Use o histórico do Git** (`git log --oneline`) para reconstruir o que fez em cada ciclo — ele é uma evidência melhor que a memória.
5. **Fale com o professor** antes do prazo, não depois.
