from pathlib import Path

import db


def test_db_path_explicit_override_in_vercel(monkeypatch, tmp_path):
    custom_path = str(tmp_path / "custom.db")
    monkeypatch.setenv("VERCEL", "1")
    monkeypatch.setenv("DB_PATH", custom_path)
    assert db._default_db_path() == custom_path


def test_db_path_uses_writable_temporary_directory_in_vercel(monkeypatch):
    monkeypatch.delenv("DB_PATH", raising=False)
    monkeypatch.setenv("VERCEL", "1")
    assert db._default_db_path() == "/tmp/midias.db"


def test_local_db_path_is_independent_of_working_directory(monkeypatch, tmp_path):
    monkeypatch.delenv("DB_PATH", raising=False)
    monkeypatch.delenv("VERCEL", raising=False)
    monkeypatch.chdir(tmp_path)
    expected = Path(db.__file__).with_name("midias.db").as_posix()
    assert db._default_db_path() == expected
