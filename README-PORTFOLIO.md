# CRUD de Filmes e Séries

Projeto pessoal e acadêmico desenvolvido para a disciplina de Algoritmos e Programação. A aplicação administra um catálogo de filmes e séries por meio de uma API web, uma interface HTML e um banco de dados SQLite.

## Objetivos

- Aplicar conceitos de lógica, algoritmos e programação em um projeto funcional.
- Implementar as operações CRUD: criar, consultar, atualizar e excluir.
- Organizar o código em camadas de API, modelos e persistência.
- Trabalhar com validação de dados, regras condicionais e tratamento de erros.
- Persistir informações em banco de dados.
- Criar testes automatizados para verificar o comportamento da aplicação.
- Conhecer uma forma de empacotar e executar o projeto com Docker.

## Metodologia utilizada

O projeto foi desenvolvido com uma abordagem **ágil, incremental e iterativa**. As funcionalidades foram implementadas e verificadas por etapas, começando pela CRUD básica e evoluindo com novos recursos:

1. Criação da API básica de filmes e séries.
2. Adição da interface web com abas.
3. Inclusão de filtros, busca, paginação e geração automática de mídias.
4. Criação da geração automática de credenciais.
5. Implementação da regra de negócio de “Vingadores: Ultimato”.
6. Migração do acesso ao banco para SQLModel ORM.
7. Criação de testes automatizados.
8. Adição da configuração Docker.
9. Correção de erros encontrados durante os testes e a execução.

Essa abordagem permitiu testar cada funcionalidade, identificar problemas e fazer ajustes durante o desenvolvimento. Não foi utilizado formalmente um framework de gestão como Scrum ou Kanban; por isso, a descrição mais adequada é abordagem ágil e incremental.

### Possível uso de Scrum ou Kanban

Embora Scrum e Kanban sejam métodos bastante utilizados em projetos de software, não houve necessidade de aplicá-los formalmente neste projeto. Por ser uma atividade individual, acadêmica e de escopo limitado, foi utilizada uma abordagem ágil, incremental e iterativa, com organização das funcionalidades por etapas.

O Scrum poderia ser utilizado caso o projeto tivesse uma equipe, reuniões de planejamento, divisão de responsabilidades e entregas organizadas em ciclos chamados sprints. Um exemplo de divisão seria:

1. Sprint 1: CRUD básica.
2. Sprint 2: interface web.
3. Sprint 3: credenciais e regras de negócio.
4. Sprint 4: testes, ORM e Docker.

O Kanban seria uma alternativa mais simples para controlar as tarefas individualmente, organizando-as em colunas como:

```text
A fazer → Em andamento → Em teste → Concluído
```

Portanto, Scrum ou Kanban poderiam ter sido utilizados, mas não eram necessários para atingir os objetivos da disciplina. Nesse contexto, uma lista organizada de tarefas e a implementação por etapas foram suficientes para acompanhar o desenvolvimento.

## Escopo do projeto

### Funcionalidades incluídas

- Cadastro de filmes e séries.
- Listagem de mídias.
- Busca por ID.
- Filtros por título, gênero e tipo.
- Paginação dos resultados.
- Atualização de campos de uma mídia.
- Exclusão de mídias.
- Geração automática de mídias fictícias.
- Geração de username único e senha aleatória.
- Armazenamento da senha usando hash `scrypt`.
- Criação automática de “Vingadores: Ultimato” quando já existe uma credencial e uma mídia.
- Testes automatizados.
- Execução local ou por Docker.

### Funcionalidades fora do escopo

- Login real de usuários.
- Sessões, tokens JWT e logout.
- Controle de permissões e perfis.
- Recuperação de senha e confirmação por e-mail.
- Implantação em servidor de produção.

## Ferramentas e tecnologias

- **Python:** linguagem principal.
- **FastAPI:** criação da API e das rotas HTTP.
- **Pydantic:** validação dos dados recebidos pela API.
- **SQLModel:** ORM que representa tabelas como classes Python.
- **SQLAlchemy:** camada utilizada pelo SQLModel para comunicação com o banco.
- **SQLite:** banco de dados local baseado em arquivo.
- **HTML, CSS e JavaScript:** interface web.
- **Pytest:** testes automatizados.
- **Uvicorn:** servidor que executa a aplicação FastAPI.
- **Docker e Docker Compose:** empacotamento e execução padronizada.
- **VS Code e Pylance:** edição, análise e diagnóstico do código.

## Conceitos de Python utilizados

- Importação de módulos e bibliotecas.
- Variáveis, constantes e valores de configuração.
- Funções com parâmetros e valores padrão.
- Tipagem com `str`, `int`, `Optional`, `Dict` e `List`.
- Classes, objetos e herança.
- Enumeração com `Enum`.
- Condicionais com `if`.
- Laços de repetição com `while` e `for`.
- Compreensão de listas.
- Dicionários no formato chave e valor.
- F-strings para formatação de textos.
- Exceções e respostas HTTP de erro.
- Gerenciadores de contexto com `with`.
- Geração segura de valores aleatórios com `secrets`.
- Hash de senhas com `hashlib.scrypt`.

## Estrutura do projeto

- `crud_filmes_e_series.py` — aplicação FastAPI, modelos de entrada e endpoints.
- `db.py` — modelos SQLModel e operações ORM do banco.
- `index.html` — interface web com as abas da aplicação.
- `seed_midias.py` — script para inserir mídias fictícias.
- `tests/test_api.py` — testes automatizados da API.
- `requirements.txt` — dependências Python.
- `Dockerfile` — imagem da aplicação.
- `docker-compose.yml` — execução da aplicação com volume persistente.
- `run.ps1` — script PowerShell para iniciar o servidor.
- `midias.db` — banco SQLite local, criado durante a execução.

## Pré-requisitos

- Python 3.8 ou superior.
- Docker Desktop, caso escolha a execução por container.

## Instalação local

No terminal, entre no diretório do projeto (`CD "caminho/para/o/diretorio/do/projeto"
`) e crie um ambiente virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate
python -m pip install -r requirements.txt
```

## Execução local

### Usando o script de inicialização

```powershell
.\run.ps1
```

### Usando o comando manual

```powershell
cd "C:\Users\DELL\Documents"
python -m uvicorn crud_filmes_e_series:app --reload
```

Acesse a interface em `http://127.0.0.1:8000` e a documentação automática em `http://127.0.0.1:8000/docs`.

## Execução com Docker

Com o Docker Desktop aberto, execute:

```powershell
docker compose up --build
```

Acesse `http://127.0.0.1:8000`. O banco ficará em `data/midias.db` e será preservado mesmo que o container seja recriado.

Para executar em segundo plano:

```powershell
docker compose up --build -d
```

Para parar:

```powershell
docker compose down
```

## Endpoints principais

- `GET /midias` — lista mídias. Aceita `limit`, `offset`, `titulo`, `genero` e `tipo`.
   O campo tipo aceita somente filme ou série.
   O campo genero   aceita apenas os valores predefinidos no sistema (ex: ação, comédia, drama, ficção científica).
- `GET /midias/{midia_id}` — busca uma mídia específica.
- `POST /midias` — cadastra uma nova mídia.
- `PUT /midias/{midia_id}` — atualiza os campos enviados.
- `DELETE /midias/{midia_id}` — exclui uma mídia.
- `POST /credenciais/gerar` — gera e salva um username e uma senha.
- `GET /credenciais` — lista usernames sem exibir senhas ou hashes.

Exemplo de corpo para `POST /midias`:

```json
{
  "titulo": "Duna",
  "tipo": "filme",
  "genero": "ficção científica",
  "ano": 2021,
  "sinopse": "Sinopse do filme"
}
```

## Regras de negócio

- O campo `tipo` aceita somente `filme` ou `série`.
- O username é gerado aleatoriamente e deve ser único.
- A senha gerada contém letras maiúsculas, minúsculas e números.
- A senha não é armazenada em texto puro; somente o hash é salvo.
- Quando há pelo menos uma credencial e uma mídia, “Vingadores: Ultimato” é criado automaticamente.
- “Vingadores: Ultimato” não é duplicado caso já exista.

## Banco de dados

O banco é SQLite e fica no arquivo `midias.db` durante a execução local. A aplicação utiliza SQLModel ORM com os modelos:

- `Midia` — representa filmes e séries.
- `Usuario` — representa as credenciais geradas.

A inicialização usa `SQLModel.metadata.create_all` e preserva tabelas e dados existentes. No Docker, a variável `DB_PATH` aponta para `/app/data/midias.db`.

## Testes automatizados

Os testes estão em `tests/test_api.py` e usam um banco SQLite temporário, sem alterar o banco principal. Execute:

```powershell
python -m pytest tests -q
```

Os testes verificam o CRUD completo, a validação de tipos, a geração de credenciais, a criação automática de “Vingadores: Ultimato” e a prevenção de duplicidade.

## Decisão sobre autenticação

A autenticação de usuários não foi implementada porque não faz parte do escopo principal da disciplina. O objetivo é demonstrar algoritmos, programação, CRUD, validação, persistência, ORM, regras condicionais e testes.

As credenciais geradas têm finalidade demonstrativa. Um sistema de login completo exigiria sessões ou tokens, proteção de rotas, logout, expiração de acesso, recuperação de senha, controle de permissões e testes adicionais.

## Limitações e melhorias futuras

- Configurar migrações versionadas com Alembic.
- Adicionar autenticação real caso o escopo seja ampliado.
- Criar diferentes perfis de acesso.
- Melhorar o tratamento de erros da interface.
- Hospedar a aplicação em um ambiente de produção.

## Uso acadêmico e portfólio

Este é um projeto pessoal e acadêmico, desenvolvido para a disciplina de Algoritmos e Programação. Ele pode ser apresentado em portfólio desde que essa finalidade seja informada claramente. O projeto demonstra conhecimentos de Python, APIs, banco de dados, ORM, interface web, testes e Docker.

