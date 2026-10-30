# Documentação histórica da API

> Este documento descreve uma versão antiga e não deve ser usado para instalar ou executar a versão atual. Consulte [DOCUMENTACAO-PORTFOLIO.md](../DOCUMENTACAO-PORTFOLIO.md).

Projeto simples em FastAPI para administrar um catálogo de filmes e séries (SQLite).

**Arquivos principais**
- `crud_filmes_e_series.py` — aplicação FastAPI (endpoints CRUD).
- `db.py` — helpers para acesso ao banco SQLite (`midias.db`).
- `seed_midias.py` — script CLI para popular o banco com mídias fictícias.
- `requirements.txt` — dependências do projeto.

Pré-requisitos
- Python 3.8+ instalado

Instalação

Abra um terminal no diretório do projeto (`C:\Users\DELL\Documents`) e crie (opcional) um ambiente virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate
python -m pip install -r requirements.txt
```

Executando a aplicação

**Opção 1: Usando o script de inicialização (recomendado)**

```powershell
.\run.ps1
```

**Opção 2: Comando manual**

```powershell
cd "C:\Users\DELL\Documents"
python -m uvicorn crud_filmes_e_series:app --reload
```

Acesse a API em `http://127.0.0.1:8000` e a documentação automática em `http://127.0.0.1:8000/docs`.

Popular o banco (seed)

Para popular com mídias de exemplo rode o script CLI (não é mais uma rota no app):

```powershell
python seed_midias.py
```

Endpoints principais

- `GET /midias` — lista mídias. Suporta query params: `limit`, `offset`, `titulo`, `genero`, `tipo`.
  - Ex.: `/midias?limit=10&offset=0`
  - Ex.: `/midias?titulo=Duna`
  - Ex.: `/midias?tipo=filme`
- `GET /midias/{midia_id}` — retorna uma mídia específica.
- `POST /midias` — cria nova mídia. Corpo JSON exemplo:

```json
{
  "titulo": "Duna",
  "tipo": "filme",
  "genero": "ficção científica",
  "ano": 2021,
  "sinopse": "Sinopse do filme"
}
```

- `PUT /midias/{midia_id}` — atualiza campos (envie apenas os campos a alterar).
- `DELETE /midias/{midia_id}` — remove uma mídia.

Validação
- O campo `tipo` é validado via `Enum` e aceita apenas `filme` ou `série`.

Banco de dados
- O arquivo SQLite criado é `midias.db` no mesmo diretório do projeto.

Próximos passos sugeridos
- Adicionar testes (`pytest`) para endpoints.
- Migrar para ORM (SQLModel/SQLAlchemy) e configurar migrações (Alembic).
- Dockerizar a aplicação para deployment consistente.


