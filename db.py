import os
from datetime import datetime
from typing import Any, Dict, List, Optional

from sqlmodel import Field, Session, SQLModel, create_engine, select

DB_PATH = os.getenv("DB_PATH", "midias.db")


class Midia(SQLModel, table=True):
    __tablename__ = "midias"

    id: Optional[int] = Field(default=None, primary_key=True)
    titulo: str
    tipo: str
    genero: Optional[str] = None
    ano: Optional[int] = None
    sinopse: Optional[str] = None
    imagem_url: Optional[str] = None


class Usuario(SQLModel, table=True):
    __tablename__ = "usuarios"

    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True, index=True)
    senha_hash: str
    criado_em: str = Field(
        default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )


def get_engine():
    return create_engine(
        f"sqlite:///{DB_PATH}",
        connect_args={"check_same_thread": False},
    )


def init_db() -> None:
    engine = get_engine()
    SQLModel.metadata.create_all(engine)

    with engine.begin() as connection:
        columns = connection.exec_driver_sql("PRAGMA table_info(midias)").fetchall()
        if not any(column[1] == "imagem_url" for column in columns):
            connection.exec_driver_sql("ALTER TABLE midias ADD COLUMN imagem_url TEXT")


def username_exists(username: str) -> bool:
    with Session(get_engine()) as session:
        return session.exec(
            select(Usuario).where(Usuario.username == username)
        ).first() is not None


def create_usuario(username: str, senha_hash: str) -> int:
    with Session(get_engine()) as session:
        usuario = Usuario(username=username, senha_hash=senha_hash)
        session.add(usuario)
        session.commit()
        session.refresh(usuario)
        usuario_id = usuario.id
    assert usuario_id is not None
    return usuario_id


def list_usuarios() -> List[Dict[str, Any]]:
    with Session(get_engine()) as session:
        usuarios = session.exec(
            select(Usuario).order_by(Usuario.id.desc())
        ).all()
        return [
            {"id": usuario.id, "username": usuario.username, "criado_em": usuario.criado_em}
            for usuario in usuarios
        ]


def ensure_filme_ultimato() -> Optional[int]:
    """Cria Vingadores: Ultimato quando já houver usuário e outra mídia."""
    with Session(get_engine()) as session:
        possui_usuario = session.exec(select(Usuario)).first() is not None
        possui_midia = session.exec(select(Midia)).first() is not None
        filme_existente = session.exec(
            select(Midia).where(Midia.titulo == "Vingadores: Ultimato")
        ).first()

        if not possui_usuario or not possui_midia or filme_existente:
            return filme_existente.id if filme_existente else None

        filme = Midia(
            titulo="Vingadores: Ultimato",
            tipo="filme",
            genero="Ação",
            ano=2019,
            sinopse="Os heróis restantes enfrentam uma última batalha para reverter o impacto do estalo.",
        )
        session.add(filme)
        session.commit()
        session.refresh(filme)
        return filme.id


def list_midias(limit: int = 100, offset: int = 0, titulo: Optional[str] = None, genero: Optional[str] = None, tipo: Optional[str] = None) -> List[Dict[str, Any]]:
    with Session(get_engine()) as session:
        query = select(Midia)
        if titulo:
            query = query.where(Midia.titulo.contains(titulo))
        if genero:
            query = query.where(Midia.genero.contains(genero))
        if tipo:
            query = query.where(Midia.tipo == tipo)
        query = query.order_by(Midia.id).offset(offset).limit(limit)
        midias = session.exec(query).all()
        return [midia.model_dump() for midia in midias]


def get_midia(midia_id: int) -> Optional[Dict[str, Any]]:
    with Session(get_engine()) as session:
        midia = session.get(Midia, midia_id)
        return midia.model_dump() if midia else None


def create_midia(data: Dict[str, Any]) -> int:
    # Normalize Enum values to strings if necessary
    tipo = data.get("tipo")
    tipo = getattr(tipo, "value", tipo)

    with Session(get_engine()) as session:
        midia = Midia(
            titulo=data.get("titulo"), tipo=tipo, genero=data.get("genero"),
            ano=data.get("ano"), sinopse=data.get("sinopse"),
            imagem_url=data.get("imagem_url"),
        )
        session.add(midia)
        session.commit()
        session.refresh(midia)
        midia_id = midia.id
    assert midia_id is not None
    return midia_id


def update_midia(midia_id: int, dados: Dict[str, Any]) -> None:
    if not dados:
        return
    # Normalize Enum values in update payload
    valores_list = []
    for v in dados.values():
        if hasattr(v, "value"):
            valores_list.append(v.value)
        else:
            valores_list.append(v)

    with Session(get_engine()) as session:
        midia = session.get(Midia, midia_id)
        if not midia:
            return
        for campo, valor in zip(dados.keys(), valores_list):
            setattr(midia, campo, valor)
        session.add(midia)
        session.commit()


def delete_midia(midia_id: int) -> None:
    with Session(get_engine()) as session:
        midia = session.get(Midia, midia_id)
        if midia:
            session.delete(midia)
            session.commit()


if __name__ == "__main__":
    init_db()
