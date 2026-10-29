import re

import pytest
from fastapi.testclient import TestClient

import db
from crud_filmes_e_series import app


@pytest.fixture()
def client(tmp_path, monkeypatch):
    monkeypatch.setattr(db, "DB_PATH", str(tmp_path / "teste.db"))
    db.init_db()
    with TestClient(app) as test_client:
        yield test_client


def test_crud_completo_de_midia(client):
    criado = client.post(
        "/midias",
        json={
            "titulo": "Duna",
            "tipo": "filme",
            "genero": "ficção científica",
            "ano": 2021,
        },
    )
    assert criado.status_code == 201
    midia_id = criado.json()["id"]

    listado = client.get("/midias?titulo=Duna")
    assert listado.status_code == 200
    assert listado.json()[0]["titulo"] == "Duna"

    atualizado = client.put(
        f"/midias/{midia_id}",
        json={"titulo": "Duna: Parte Um"},
    )
    assert atualizado.status_code == 200

    buscado = client.get(f"/midias/{midia_id}")
    assert buscado.json()["titulo"] == "Duna: Parte Um"

    removido = client.delete(f"/midias/{midia_id}")
    assert removido.status_code == 200
    assert client.get(f"/midias/{midia_id}").status_code == 404


def test_geracao_de_credenciais(client):
    resposta = client.post("/credenciais/gerar")

    assert resposta.status_code == 201
    credencial = resposta.json()
    senha = credencial["senha"]
    assert re.fullmatch(r"cineuser\d{6}", credencial["username"])
    assert len(senha) == 12
    assert any(caractere.islower() for caractere in senha)
    assert any(caractere.isupper() for caractere in senha)
    assert any(caractere.isdigit() for caractere in senha)

    usuarios = client.get("/credenciais")
    assert usuarios.status_code == 200
    assert usuarios.json()[0]["username"] == credencial["username"]
    assert "senha" not in usuarios.json()[0]
    assert "senha_hash" not in usuarios.json()[0]


def test_validacao_rejeita_tipo_invalido(client):
    resposta = client.post(
        "/midias", json={"titulo": "Exemplo", "tipo": "documentário"}
    )

    assert resposta.status_code == 422


def test_cria_ultimato_depois_de_credencial_e_midia(client):
    assert client.post("/credenciais/gerar").status_code == 201
    assert client.post(
        "/midias", json={"titulo": "Interestelar", "tipo": "filme"}
    ).status_code == 201

    filmes = client.get("/midias?titulo=Vingadores").json()
    assert len(filmes) == 1
    assert filmes[0]["titulo"] == "Vingadores: Ultimato"
    assert filmes[0]["tipo"] == "filme"


def test_ultimato_nao_e_duplicado(client):
    client.post("/credenciais/gerar")
    client.post("/midias", json={"titulo": "Matrix", "tipo": "filme"})
    client.post("/midias", json={"titulo": "Avatar", "tipo": "filme"})

    filmes = client.get("/midias?titulo=Vingadores").json()
    assert len(filmes) == 1