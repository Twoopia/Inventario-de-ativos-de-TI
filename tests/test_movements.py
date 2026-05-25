from fastapi.testclient import TestClient


def test_create_movement(client: TestClient, auth_headers: dict):
    # Garante que há um ativo com ID 1
    asset_payload = {
        "tag": "MOV-001",
        "name": "Ativo para movimentação",
        "status": "ativo",
        "location": "Almoxarifado",
    }
    client.post("/api/v1/assets/", json=asset_payload, headers=auth_headers)

    payload = {
        "asset_id": 1,
        "movement_type": "transferencia",
        "from_location": "Almoxarifado",
        "to_location": "Sala 101",
        "notes": "Transferência para novo colaborador",
    }
    response = client.post("/api/v1/movements/", json=payload, headers=auth_headers)
    assert response.status_code == 201
    data = response.json()
    assert data["movement_type"] == "transferencia"
    assert data["to_location"] == "Sala 101"


def test_get_asset_movements(client: TestClient, auth_headers: dict):
    response = client.get("/api/v1/movements/asset/1", headers=auth_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_recent_movements(client: TestClient, auth_headers: dict):
    response = client.get("/api/v1/movements/recent", headers=auth_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_movement_not_found_asset(client: TestClient, auth_headers: dict):
    payload = {
        "asset_id": 99999,
        "movement_type": "atribuicao",
    }
    response = client.post("/api/v1/movements/", json=payload, headers=auth_headers)
    assert response.status_code == 404
