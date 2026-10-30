# CRUD de Filmes e Séries — documentação de portfólio

Aplicação de estudo para gerenciar um catálogo de filmes e séries, desenvolvida a partir da disciplina de **Algoritmos e Programação**, ministrada por **Rondineli Seba Salomão**, na UNDB. A versão de portfólio reúne uma API em Python, uma interface web e persistência local com SQLite.

Desenvolvido por **Pedro Lucas Pereira Rolim**, estudante de Sistemas de Informação, com interesse em atuar e aprofundar seus conhecimentos em **desenvolvimento front-end**.

## Veja a aplicação

- [Abrir demonstração](https://algoritmos-e-programa-o.vercel.app/).
- [Explorar a documentação interativa da API](https://algoritmos-e-programa-o.vercel.app/docs).
- [README principal](../README.md): organização do repositório e acesso aos três ciclos acadêmicos.

![Tela do CRUD com navegação por abas, filtros de mídias e início de uma capa SVG de ficção científica](images/crud-interface.png)

*Captura da interface de listagem fornecida pelo autor. Os dados do catálogo podem mudar; a demonstração hospedada usa armazenamento temporário.*

## Objetivo e contribuição para meu aprendizado

Meu objetivo foi transformar os conceitos de lógica de programação em um catálogo no qual fosse possível cadastrar, consultar, atualizar e excluir informações. Ao ampliar o projeto, também tive contato com a comunicação entre uma interface web, uma API e um banco de dados.

| Aprendizado | Como aparece no projeto |
|---|---|
| Variáveis e operadores | Representação dos dados de uma mídia, comparações e cálculos usados nas operações. |
| Condicionais | Validação de entradas, verificação de registros e decisões durante o cadastro. |
| Laços de repetição | Percorrer coleções, apresentar resultados e repetir operações nas versões de terminal. |
| Estruturas dinâmicas | Organização de coleções e dados com listas e dicionários, conforme a etapa estudada. |
| Funções e refatoração | Divisão das tarefas em partes menores e organização das operações do CRUD. |
| Integração de uma aplicação web | Contato com requisições HTTP, respostas da API e atualização da interface. |
| Qualidade e tratamento de falhas | Testes com bancos temporários, validações e capas alternativas quando uma imagem não carrega. |
| Organização e escopo | Uso de branches para apresentar os ciclos e distinguir os requisitos acadêmicos das ampliações pessoais. |

Esses pontos representam conteúdos praticados e conhecimentos em desenvolvimento. A presença de uma tecnologia no projeto não significa domínio completo dela; o repositório também registra o que ainda preciso aprofundar.

## Minha decisão de criar o front-end

O professor não havia solicitado uma interface web. Decidi adicioná-la para visualizar o catálogo, interagir com os dados por formulários e experimentar a apresentação da aplicação. Essa escolha ampliou o projeto além do escopo da disciplina.

Depois de compreender melhor os limites de cada ciclo, organizei branches didáticas alinhadas ao conteúdo pedido. Elas apresentam versões para avaliação acadêmica; a aplicação ampliada foi mantida como uma evolução de estudo e portfólio.

Ao trabalhar com o visual, as abas, os formulários e as capas, descobri afinidade com o desenvolvimento front-end. Essa experiência ajudou a direcionar meu objetivo profissional: pretendo trabalhar nessa área e aprofundar meus conhecimentos em HTML, CSS, JavaScript, acessibilidade, responsividade e experiência de uso.

Também aprendi que explorar uma ideia pessoal e cumprir os requisitos de uma entrega são responsabilidades que precisam ser organizadas. O front-end passou a ter um lugar próprio na evolução do projeto, enquanto as branches dos ciclos documentam o recorte solicitado.

## Escopo acadêmico e versão atual

| Etapa | Recorte da disciplina | Onde consultar |
|---|---|---|
| Ciclo 1 | Variáveis, operadores, condicionais e laços. | [ciclo-1--terminal](https://github.com/pedruck9-crypto/algoritmos-e-programacao/tree/ciclo-1--terminal) |
| Ciclo 2 | Refatoração e estruturas dinâmicas, como listas, matrizes, mapas e dicionários, conforme o conteúdo estudado. | [ciclo-2-estruturas-dinâmicas](https://github.com/pedruck9-crypto/algoritmos-e-programacao/tree/ciclo-2-estruturas-din%C3%A2micas) |
| Ciclo 3 | Organização do código em funções e aplicação final dentro do escopo combinado. | [ciclo-3-funções](https://github.com/pedruck9-crypto/algoritmos-e-programacao/tree/ciclo-3-fun%C3%A7%C3%B5es) |

A interface web, o FastAPI, o ORM, o banco SQLite, as capas SVG, os testes e a configuração Docker pertencem à **versão ampliada de portfólio**. Eles não são apresentados como exigências da disciplina. As branches didáticas foram organizadas após a ampliação e não representam necessariamente a ordem histórica em que o código foi escrito.

## Funcionalidades centrais

- Criar, listar, buscar por ID, atualizar e excluir mídias.
- Filtrar por título, gênero e tipo, com `limit` e `offset` na API.
- Gerar sugestões fictícias de mídias na interface e salvá-las no catálogo.
- Registrar URL de imagem/poster para cada mídia.
- Gerar capas SVG por código, com título, gênero, ano, paleta e ilustração geométrica. A mesma mídia mantém uma composição consistente.
- Exibir uma capa SVG alternativa quando faltar imagem ou houver falha no carregamento, na listagem, busca por ID e prévia do gerador.

## Exercícios adicionais de regras de negócio

As funcionalidades abaixo foram acrescentadas como exercícios de condições, geração de valores e armazenamento. O objetivo central do projeto continua sendo o gerenciamento do catálogo.

- Usar o [pôster indicado de Vingadores: Ultimato](https://ovicio.com.br/wp-content/uploads/2019/03/20190326-avengers-endgame-cast-poster-730x365.jpg) no cadastro automático. Registros antigos desse título sem imagem recebem esse endereço na inicialização; imagens personalizadas existentes são preservadas.
- Gerar credenciais demonstrativas: username único, senha aleatória de 12 caracteres e hash `scrypt` com salt. A senha é retornada uma única vez; a listagem não expõe senha nem hash.
- Criar “Vingadores: Ultimato” após cadastrar uma mídia ou gerar uma credencial, quando houver pelo menos uma mídia e um usuário. A regra consulta se o título já existe antes de inserir.

As credenciais são um exercício de geração e armazenamento de valores. Não existe login, sessão, token ou proteção de rotas. Os registros da demonstração são compartilhados entre visitantes.

## Tecnologias e estrutura

Python 3.12 ou superior, FastAPI, Pydantic, SQLModel/SQLAlchemy, SQLite, HTML, CSS, JavaScript, Uvicorn, Pytest e HTTPX2. **Docker e Docker Compose estão configurados, mas sua execução ainda não foi realizada nem validada.**

| Arquivo/pasta | Responsabilidade |
|---|---|
| `crud_filmes_e_series.py` | API, validação de entrada e geração de credenciais. |
| `db.py` | Modelos `Midia` e `Usuario`, persistência e regra de “Vingadores: Ultimato”. |
| `index.html` | Interface e gerador de sugestões fictícias. |
| `seed_midias.py` | Inserção de cinco mídias de exemplo. |
| `tests/` | Testes da API e da escolha do caminho do banco. |
| `AULAS/` | Exercícios independentes da disciplina, descritos em seu próprio README. |
| `docs/` | Documentação atual e histórico de documentação em `historico/`. |
| `requirements.txt` | Dependências para execução e testes locais. |
| `pyproject.toml` | Requisito de Python, dependências de execução e entrada da Vercel. |
| `run.ps1` / `run.sh` | Inicialização local a partir da pasta do projeto. |
| `Dockerfile` / `docker-compose.yml` | Execução em container com banco em volume local. |

## Instalação e execução local

Para executar a versão principal documentada nesta página, clone a branch `main`:

```text
git clone --branch main https://github.com/pedruck9-crypto/algoritmos-e-programacao.git
cd algoritmos-e-programacao
python -m venv .venv
```

Ative o ambiente no PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Ou no Linux/macOS:

```bash
source .venv/bin/activate
```

Instale as dependências e inicie a aplicação na pasta do projeto:

```text
python -m pip install -r requirements.txt
python -m uvicorn crud_filmes_e_series:app --reload
```

Também é possível executar `./run.ps1` no PowerShell ou `bash run.sh` no Linux/macOS, com o ambiente virtual ativado.

Abra a [interface local](http://127.0.0.1:8000) ou a [documentação interativa da API](http://127.0.0.1:8000/docs). A interface usa URLs relativas para acessar a API no mesmo domínio. Abra a interface pelo servidor, em vez de abrir o HTML diretamente como arquivo.

Para inserir exemplos:

```text
python seed_midias.py
```

O seed insere cinco mídias a cada execução; repeti-lo pode gerar duplicatas desses exemplos.

## Banco de dados e implantação

O caminho é escolhido nesta ordem:

1. `DB_PATH`, se definido, permite configurar o arquivo SQLite; a pasta de destino deve existir e permitir escrita.
2. Na Vercel (`VERCEL` definido), usa `/tmp/midias.db`.
3. Localmente, cria `midias.db` ao lado de `db.py`, independentemente da pasta de onde o processo foi iniciado.

O banco é gerado durante a execução e não é versionado. Use o seed para obter dados de exemplo.

A demonstração está em [algoritmos-e-programa-o.vercel.app](https://algoritmos-e-programa-o.vercel.app/). O armazenamento em `/tmp` é temporário e pode variar entre instâncias ou desaparecer quando a função reiniciar. Essa implantação não garante persistência durável nem um catálogo consistente entre instâncias. Um serviço de banco persistente é uma melhoria futura.

Esta versão usa as tabelas `midias` e `usuarios`. Versões anteriores da `main` usavam `midia` e `credencial`; os dados dessas tabelas não são migrados automaticamente. Caso mantenha um banco antigo com dados importantes, faça uma cópia e planeje a migração antes de trocar de versão. A inicialização cria as tabelas atuais e acrescenta `imagem_url` a uma tabela `midias` antiga, se necessário.

## Docker — configuração ainda não executada

**Situação: os arquivos `Dockerfile` e `docker-compose.yml` estão presentes, mas o build e a execução em container ainda não foram realizados.** Portanto, essa forma de execução está pendente de validação e não deve ser apresentada como um resultado já testado.

O procedimento previsto, a conferir em um ambiente com Docker e Docker Compose disponíveis, é executar na pasta do projeto:

```text
docker compose up --build
```

A configuração prevê a interface em `http://127.0.0.1:8000`. O Compose configura `DB_PATH=/app/data/midias.db` e monta `./data` para preservar o banco local entre recriações do container.

Para parar:

```text
docker compose down
```

## API

| Método e caminho | Função |
|---|---|
| `GET /midias` | Listar; aceita `limit`, `offset`, `titulo`, `genero` e `tipo`. |
| `GET /midias/{midia_id}` | Consultar por ID. |
| `POST /midias` | Criar uma mídia. |
| `PUT /midias/{midia_id}` | Atualizar os campos enviados e não nulos. |
| `DELETE /midias/{midia_id}` | Excluir uma mídia. |
| `POST /credenciais/gerar` | Gerar e salvar username e hash; retornar a senha uma vez. |
| `GET /credenciais` | Listar ID, username e data de criação. |

Exemplo de corpo para `POST /midias`:

```json
{
  "titulo": "Duna",
  "tipo": "filme",
  "genero": "ficção científica",
  "ano": 2021,
  "sinopse": "Um jovem herdeiro luta pelo controle de Arrakis."
}
```

O cadastro e a atualização validam `tipo` como `filme` ou `série`. O gênero aceita texto livre. O ano, quando informado, deve estar entre 1900 e 2100. `imagem_url` é opcional e armazenada como texto.

## Testes e evidências de validação

Na validação registrada da [versão `bdb876b`](https://github.com/pedruck9-crypto/algoritmos-e-programacao/commit/bdb876b714a686ed163109d02e173715591026b3), **11 testes Python e 7 testes JavaScript passaram** em ambiente local, com Python 3.14 e Node.js 24. Também foi conferido no navegador o carregamento de uma capa SVG, a troca de uma imagem quebrada pela alternativa e a exibição do pôster de “Vingadores: Ultimato”. Esse registro não substitui uma nova execução após mudanças futuras.

A configuração exige Python 3.12 ou superior; a execução com Python 3.12 e com Docker ainda precisa ser validada separadamente. Os comandos abaixo permitem reproduzir as verificações.

Com as dependências instaladas, execute na raiz do projeto:

```text
python -m pytest tests -q
```

Os testes da API usam um banco temporário por teste, incluindo durante a primeira importação da aplicação. Cobrem a interface servida a partir de outra pasta de trabalho, CRUD, rejeição de tipo inválido, geração/listagem de credenciais e criação de “Vingadores: Ultimato” sem duplicação em chamadas sequenciais. Os testes de configuração verificam o caminho local, a Vercel e a prioridade de `DB_PATH`.

As verificações do gerador e da troca de imagens podem ser executadas com Node.js instalado (necessário apenas para estes testes, não para executar o CRUD):

```text
node --test tests/test_covers.cjs
```

Essas verificações cobrem consistência das capas, caracteres especiais, imagens ausentes, preservação de URLs externas e troca para a alternativa sem repetição de erro.

## Limitações atuais

- A demonstração hospedada ainda não possui persistência durável.
- Não há migrações versionadas para preservar dados entre alterações de esquema.
- Autenticação e controle de permissões ainda não estão implementados.
- A regra de “Vingadores: Ultimato” ainda precisa de proteção contra inserções simultâneas; a consulta atual não garante unicidade em concorrência.
- A paginação da interface, o tratamento de erros e a exibição de conteúdo fornecido pelo usuário ainda precisam de melhorias.
- As capas SVG são composições gráficas geradas por código, não ilustrações de IA. Imagens externas, incluindo o pôster de Vingadores, podem ficar indisponíveis; nesse caso a interface usa a alternativa SVG.

## Como pretendo evoluir durante o curso

A evolução será feita por etapas, conforme eu consolidar os fundamentos e estudar novos conteúdos. Os itens abaixo são planos; não representam funcionalidades já implementadas.

| Etapa de aprendizado | Evolução pretendida | Resultado a verificar |
|---|---|---|
| Fundamentos de front-end | Melhorar HTML semântico, formulários, navegação por teclado, contraste, responsividade e feedback de carregamento/erro. | Uma interface mais acessível e utilizável em diferentes tamanhos de tela. |
| JavaScript e organização | Separar responsabilidades da interface, corrigir a navegação entre páginas e aprofundar a integração com a API. | Código mais fácil de entender e comportamento consistente durante o uso. |
| Banco de dados | Estudar PostgreSQL e migrações versionadas, além do SQLite usado atualmente. | Dados preservados entre implantações e mudanças de esquema. |
| Segurança e aplicações web | Implementar autenticação e autorização por proprietário. | Cada pessoa acessar somente seu catálogo e suas operações. |
| Testes e implantação | Automatizar os testes no GitHub, validar Python 3.12 e executar o Docker. | Verificações reproduzíveis para alterações futuras. |
| Ferramentas de front-end | Avaliar TypeScript e um framework de componentes depois de fortalecer HTML, CSS e JavaScript. | Componentes organizados com uma escolha técnica que eu consiga explicar. |
| Integrações externas e IA | Estudar geração opcional de capas, armazenamento persistente de imagens, filas de tarefas e controle de custos. | Uma integração protegida e recuperável, mantendo a capa SVG alternativa. |

O plano mais detalhado de IA, autenticação e PostgreSQL está na [branch de evolução futura](https://github.com/pedruck9-crypto/algoritmos-e-programacao/blob/Crud_com_imagens_geradas_por_ia_e_autenticacao/README.md). A versão atual não usa IA para gerar capas nem possui login real.

Meu foco profissional é o **front-end**. Quero usar este projeto para acompanhar meu aprendizado e demonstrar, em oportunidades de estágio ou início de carreira, a evolução da interface e minha capacidade de compreender sua integração com o restante da aplicação.

O projeto é uma aplicação de estudo e demonstração de portfólio, em evolução.
