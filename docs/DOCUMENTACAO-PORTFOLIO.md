# CRUD de Filmes e Séries — documentação de portfólio

Aplicação de estudo para gerenciar um catálogo de filmes e séries. O projeto nasceu na disciplina de Algoritmos e Programação e foi ampliado com uma API, interface web e banco de dados. Consulte o [README principal](../README.md) para acessar os três ciclos didáticos.

## Funcionalidades

- Criar, listar, buscar por ID, atualizar e excluir mídias.
- Filtrar por título, gênero e tipo, com `limit` e `offset` na API.
- Gerar sugestões fictícias de mídias na interface e salvá-las no catálogo.
- Registrar URL de imagem/poster para cada mídia.
- Gerar capas SVG por código, com título, gênero, ano, paleta e ilustração geométrica. A mesma mídia mantém uma composição consistente.
- Exibir uma capa SVG alternativa quando faltar imagem ou houver falha no carregamento, na listagem, busca por ID e prévia do gerador.
- Usar o [pôster indicado de Vingadores: Ultimato](https://ovicio.com.br/wp-content/uploads/2019/03/20190326-avengers-endgame-cast-poster-730x365.jpg) no cadastro automático. Registros antigos desse título sem imagem recebem esse endereço na inicialização; imagens personalizadas existentes são preservadas.
- Gerar credenciais demonstrativas: username único, senha aleatória de 12 caracteres e hash `scrypt` com salt. A senha é retornada uma única vez; a listagem não expõe senha nem hash.
- Criar “Vingadores: Ultimato” após cadastrar uma mídia ou gerar uma credencial, quando houver pelo menos uma mídia e um usuário. A regra consulta se o título já existe antes de inserir.

As credenciais são um exercício de geração e armazenamento de valores. Não existe login, sessão, token ou proteção de rotas. Os registros da demonstração são compartilhados entre visitantes.

## Tecnologias e estrutura

Python 3.12 ou superior, FastAPI, Pydantic, SQLModel/SQLAlchemy, SQLite, HTML, CSS, JavaScript, Uvicorn, Pytest e HTTPX2. Há configuração para Docker e Docker Compose.

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

Clone o repositório e entre na pasta correspondente à versão que deseja executar. Para esta branch:

```text
git clone --branch "Crud_portfólio" https://github.com/pedruck9-crypto/algoritmos-e-programa-o-.git
cd algoritmos-e-programa-o-
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

## Docker

Com Docker e Docker Compose disponíveis, execute na pasta do projeto:

```text
docker compose up --build
```

A interface fica em `http://127.0.0.1:8000`. O Compose configura `DB_PATH=/app/data/midias.db` e monta `./data` para preservar o banco local entre recriações do container.

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

## Testes

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

## Limitações e próximos passos

- Persistência durável para a demonstração hospedada.
- Migrações versionadas para preservar dados entre alterações de esquema.
- Autenticação e permissões, caso se tornem requisitos.
- Proteção contra inserções simultâneas da regra de “Vingadores: Ultimato”; a consulta atual não é uma garantia de unicidade em concorrência.
- Melhorias na paginação da interface, no tratamento de erros e na exibição de conteúdo fornecido pelo usuário.
- As capas SVG são composições gráficas geradas por código, não ilustrações de IA. Imagens externas, incluindo o pôster de Vingadores, podem ficar indisponíveis; nesse caso a interface usa a alternativa SVG.

O projeto é uma aplicação de estudo e demonstração de portfólio, em evolução.
