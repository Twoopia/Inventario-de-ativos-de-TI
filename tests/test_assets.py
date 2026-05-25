import pytest
from fastapi.testclient import TestClient


def test_create_asset(client: TestClient, auth_headers: dict):
    payload = {
        "tag": "TI-001",
        "name": "Notebook Dell Latitude",
        "brand": "Dell",
        "model": "Latitude 5420",
        "serial_number": "SN123456",
        "status": "ativo",
        "location": "Sala TI",
    }
    response = client.post("/api/v1/assets/", json=payload, headers=auth_headers)
    assert response.status_code == 201
    data = response.json()
    assert data["tag"] == "TI-001"
    assert data["name"] == "Notebook Dell Latitude"


def test_create_asset_duplicate_tag(client: TestClient, auth_headers: dict):
    payload = {"tag": "TI-001", "name": "Outro Notebook", "status": "ativo"}
    response = client.post("/api/v1/assets/", json=payload, headers=auth_headers)
    assert response.status_code == 409


def test_list_assets(client: TestClient, auth_headers: dict):
    response = client.get("/api/v1/assets/", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert "items" in data
    assert "total" in data
    assert data["total"] >= 1


def test_get_asset(client: TestClient, auth_headers: dict):
    response = client.get("/api/v1/assets/1", headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_update_asset(client: TestClient, auth_headers: dict):
    payload = {"location": "Sala de Reuniões"}
    response = client.put("/api/v1/assets/1", json=payload, headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["location"] == "Sala de Reuniões"


def test_update_asset_status(client: TestClient, auth_headers: dict):
    response = client.patch(
        "/api/v1/assets/1/status",
        params={"status": "manutencao"},
        headers=auth_headers,
    )
    assert response.status_code == 200
    assert response.json()["status"] == "manutencao"


def test_search_assets(client: TestClient, auth_headers: dict):
    response = client.get(
        "/api/v1/assets/",
        params={"search": "Dell"},
        headers=auth_headers,
    )
    assert response.status_code == 200
    assert response.json()["total"] >= 1


def test_export_csv(client: TestClient, auth_headers: dict):
    response = client.get("/api/v1/assets/export/csv", headers=auth_headers)
    assert response.status_code == 200
    assert "text/csv" in response.headers["content-type"]


def test_get_asset_not_found(client: TestClient, auth_headers: dict):
    response = client.get("/api/v1/assets/99999", headers=auth_headers)
    assert response.status_code == 404


def test_unauthorized_without_token(client: TestClient):
    response = client.get("/api/v1/assets/")
    assert response.status_code == 401
