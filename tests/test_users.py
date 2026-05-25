import pytest
from fastapi.testclient import TestClient


def test_login_success(client: TestClient, auth_headers: dict):
    # auth_headers fixture already validates login works
    assert auth_headers is not None


def test_login_wrong_password(client: TestClient):
    response = client.post(
        "/api/v1/auth/token",
        data={"username": "test@admin.com", "password": "wrongpassword"},
    )
    assert response.status_code == 401


def test_get_me(client: TestClient, auth_headers: dict):
    response = client.get("/api/v1/auth/me", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@admin.com"
    assert data["is_admin"] is True


def test_create_user(client: TestClient, auth_headers: dict):
    payload = {
        "name": "João Silva",
        "email": "joao@empresa.com",
        "password": "Senha@123",
        "department": "Financeiro",
        "is_admin": False,
    }
    response = client.post("/api/v1/users/", json=payload, headers=auth_headers)
    assert response.status_code == 201
    assert response.json()["email"] == "joao@empresa.com"


def test_list_users(client: TestClient, auth_headers: dict):
    response = client.get("/api/v1/users/", headers=auth_headers)
    assert response.status_code == 200
    assert len(response.json()) >= 1


def test_get_user_not_found(client: TestClient, auth_headers: dict):
    response = client.get("/api/v1/users/99999", headers=auth_headers)
    assert response.status_code == 404
