import os
from pathlib import Path
from typing import Any, Optional

from sqlmodel import Field, SQLModel, Session, create_engine, select


class Midia(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    titulo: str
    tipo: str
    genero: Optional[str] = None
    ano: Optional[int] = None
    sinopse: Optional[str] = None


def _database_url() -> str:
    # Vercel functions have a read-only deployment filesystem; /tmp is writable
    # but temporary. Locally, keep the database beside this module.
    if os.getenv("VERCEL"):
        db_path = Path("/tmp/midias.db")
    else:
        db_path = Path(__file__).with_name("midias.db")
    return f"sqlite:///{db_path.as_posix()}"


engine = create_engine(
    _database_url(),
    connect_args={"check_same_thread": False},
)


def init_db() -> None:
    SQLModel.metadata.create_all(engine)


def _to_dict(midia: Midia) -> dict[str, Any]:
    return midia.model_dump()


def list_midias(
    limit: int = 100,
    offset: int = 0,
    titulo: Optional[str] = None,
    genero: Optional[str] = None,
    tipo: Optional[str] = None,
) -> list[dict[str, Any]]:
    statement = select(Midia)
    if titulo:
        statement = statement.where(Midia.titulo.ilike(f"%{titulo}%"))
    if genero:
        statement = statement.where(Midia.genero.ilike(f"%{genero}%"))
    if tipo:
        statement = statement.where(Midia.tipo == tipo)
    statement = statement.order_by(Midia.id).offset(offset).limit(limit)
    with Session(engine) as session:
        return [_to_dict(item) for item in session.exec(statement).all()]


def get_midia(midia_id: int) -> Optional[dict[str, Any]]:
    with Session(engine) as session:
        item = session.get(Midia, midia_id)
        return _to_dict(item) if item else None


def create_midia(dados: dict[str, Any]) -> int:
    valores = dict(dados)
    tipo = valores.get("tipo")
    if hasattr(tipo, "value"):
        valores["tipo"] = tipo.value
    item = Midia(**valores)
    with Session(engine) as session:
        session.add(item)
        session.commit()
        session.refresh(item)
        return int(item.id)


def update_midia(midia_id: int, dados: dict[str, Any]) -> None:
    with Session(engine) as session:
        item = session.get(Midia, midia_id)
        if item is None:
            return
        for campo, valor in dados.items():
            if campo == "tipo" and hasattr(valor, "value"):
                valor = valor.value
            setattr(item, campo, valor)
        session.add(item)
        session.commit()


def delete_midia(midia_id: int) -> None:
    with Session(engine) as session:
        item = session.get(Midia, midia_id)
        if item is not None:
            session.delete(item)
            session.commit()
