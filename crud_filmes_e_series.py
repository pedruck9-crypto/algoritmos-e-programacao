from typing import Optional
from enum import Enum
from fastapi import FastAPI, HTTPException, Query, Path
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from db import init_db, list_midias, get_midia, create_midia as db_create_midia, update_midia as db_update_midia, delete_midia as db_delete_midia, create_credential as db_create_credential, list_credentials as db_list_credentials


app = FastAPI(
    title="CRUD de Filmes e Séries",
    description="API para gerenciar um catálogo de filmes e séries",
    version="1.0.0"
)

# Configurar CORS para permitir requisições do frontend HTML
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_class=HTMLResponse, tags=["Home"])
def read_root():
    """Retorna a página inicial com interface de usuário."""
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()


init_db()


class MidiaCreate(BaseModel):
    titulo: str = Field(..., min_length=1, description="Título do filme ou série")
    
    class Tipo(str, Enum):
        filme = "filme"
        serie = "série"

    tipo: Tipo = Field(..., description="Tipo de mídia: filme ou série")
    genero: Optional[str] = Field(None, description="Gênero (ex: ficção, drama, ação)")
    ano: Optional[int] = Field(None, ge=1900, le=2100, description="Ano de lançamento")
    sinopse: Optional[str] = Field(None, description="Descrição breve do conteúdo")

    class Config:
        json_schema_extra = {
            "example": {
                "titulo": "Duna",
                "tipo": "filme",
                "genero": "ficção científica",
                "ano": 2021,
                "sinopse": "Um jovem herdeiro luta pelo controle do planeta Arrakis."
            }
        }


class MidiaUpdate(BaseModel):
    titulo: Optional[str] = Field(None, min_length=1, description="Título do filme ou série")
    tipo: Optional[MidiaCreate.Tipo] = Field(None, description="Tipo de mídia: filme ou série")
    genero: Optional[str] = Field(None, description="Gênero (ex: ficção, drama, ação)")
    ano: Optional[int] = Field(None, ge=1900, le=2100, description="Ano de lançamento")
    sinopse: Optional[str] = Field(None, description="Descrição breve do conteúdo")

@app.get("/midias", tags=["Mídias"])
def listar_midias(
    limit: int = Query(100, ge=1, le=1000, description="Máximo de itens a retornar"),
    offset: int = Query(0, ge=0, description="Deslocamento para paginação"),
    titulo: Optional[str] = Query(None, description="Busca parcial no título"),
    genero: Optional[str] = Query(None, description="Busca parcial no gênero"),
    tipo: Optional[str] = Query(None, description="Filtro por tipo (filme/série)")
):
    """Listar todas as mídias com suporte a paginação e filtros.
    
    Retorna uma lista de mídias ordenadas por ID.
    Use `limit` e `offset` para paginação.
    Use `titulo`, `genero` ou `tipo` para filtrar resultados.
    """
    return list_midias(limit=limit, offset=offset, titulo=titulo, genero=genero, tipo=tipo)

@app.get("/midias/{midia_id}", tags=["Mídias"])
def buscar_midia(midia_id: int = Path(..., ge=1, description="ID da mídia")):
    """Buscar uma mídia específica pelo ID."""
    row = get_midia(midia_id)
    if not row:
        raise HTTPException(status_code=404, detail=f"Mídia com ID {midia_id} não encontrada")
    return row

@app.post("/midias", status_code=201, tags=["Mídias"])
def criar_midia(midia: MidiaCreate):
    """Criar uma nova mídia (filme ou série) no banco."""
    midia_id = db_create_midia(midia.dict())
    return {"id": midia_id, **midia.dict()}

@app.put("/midias/{midia_id}", tags=["Mídias"])
def atualizar_midia(midia_id: int = Path(..., ge=1, description="ID da mídia"), dados: MidiaUpdate = None):
    """Atualizar campos de uma mídia existente.
    
    Envie apenas os campos que deseja alterar.
    """
    atual = get_midia(midia_id)
    if not atual:
        raise HTTPException(status_code=404, detail=f"Mídia com ID {midia_id} não encontrada")

    dados_dict = {k: v for k, v in dados.dict().items() if v is not None}
    if not dados_dict:
        raise HTTPException(status_code=400, detail="Nenhum campo para atualizar fornecido")

    db_update_midia(midia_id, dados_dict)
    return {"mensagem": "Mídia atualizada com sucesso"}

@app.delete("/midias/{midia_id}", tags=["Mídias"])
def deletar_midia(midia_id: int = Path(..., ge=1, description="ID da mídia")):
    """Remover uma mídia do banco."""
    row = get_midia(midia_id)
    if not row:
        raise HTTPException(status_code=404, detail=f"Mídia com ID {midia_id} não encontrada")

    db_delete_midia(midia_id)
    return {"mensagem": f"Mídia com ID {midia_id} removida com sucesso"}


@app.post("/credenciais/gerar", status_code=201, tags=["Credenciais"])
def gerar_credencial():
    """Gerar uma credencial de demonstração; isso não cria uma conta autenticável."""
    return db_create_credential()


@app.get("/credenciais", tags=["Credenciais"])
def listar_credenciais():
    """Listar nomes de usuário gerados, sem expor hashes ou senhas."""
    return db_list_credentials()
