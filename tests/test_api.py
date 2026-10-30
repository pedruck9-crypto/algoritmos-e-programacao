import re

import pytest
from fastapi.testclient import TestClient

import db


@pytest.fixture()
def client(tmp_path, monkeypatch):
    monkeypatch.setattr(db, "DB_PATH", str(tmp_path / "teste.db"))
    from crud_filmes_e_series import app

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
    assert filmes[0]["imagem_url"] == db.ULTIMATO_IMAGE_URL


def test_ultimato_nao_e_duplicado(client):
    client.post("/credenciais/gerar")
    client.post("/midias", json={"titulo": "Matrix", "tipo": "filme"})
    client.post("/midias", json={"titulo": "Avatar", "tipo": "filme"})

    filmes = client.get("/midias?titulo=Vingadores").json()
    assert len(filmes) == 1

def test_interface_independe_da_pasta_de_trabalho(client, monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)
    resposta = client.get("/")
    assert resposta.status_code == 200
    assert "CRUD de Filmes e Séries" in resposta.text


def test_imagem_ultimato_antigo_e_preenchida_sem_duplicar(client):
    midia_id = db.create_midia({"titulo": "Vingadores: Ultimato", "tipo": "filme"})
    db.init_db()
    db.init_db()
    filmes = client.get("/midias?titulo=Vingadores").json()
    assert len(filmes) == 1
    assert filmes[0]["id"] == midia_id
    assert filmes[0]["imagem_url"] == db.ULTIMATO_IMAGE_URL


def test_imagem_personalizada_ultimato_e_preservada(client):
    url = "https://example.com/capa-escolhida.jpg"
    midia_id = db.create_midia({"titulo": "Vingadores: Ultimato", "tipo": "filme", "imagem_url": url})
    db.init_db()
    assert db.get_midia(midia_id)["imagem_url"] == url
