
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"mensagem": "Bem-vindo ao Guia do Sobrevivente Solitário"}

def test_orcamento_endpoint():
    response = client.get("/orcamento/?salario=5000")
    assert response.status_code == 200
    assert response.json() == {
        "moradia": 2000.0,
        "alimentacao": 1500.0,
        "lazer": 1000.0,
        "outros": 500.0
    }

def test_orcamento_com_filtros():
    response = client.get("/orcamento/?salario=5000&categorias=moradia&categorias=lazer")
    assert response.status_code == 200
    assert response.json() == {
        "moradia": 2000.0,
        "lazer": 1000.0
    }

def test_auth_middleware_fails():
    response = client.get("/", headers={})  # Sem o cabeçalho de autorização
    assert response.status_code == 401
    assert response.json() == {"detail": "Autorização necessária"}
