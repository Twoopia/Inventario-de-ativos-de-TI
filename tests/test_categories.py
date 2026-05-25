from fastapi.testclient import TestClient


def test_create_category(client: TestClient, auth_headers: dict):
    payload = {"name": "Notebook Test", "description": "Categoria de teste"}
    response = client.post("/api/v1/categories/", json=payload, headers=auth_headers)
    assert response.status_code == 201
    assert response.json()["name"] == "Notebook Test"


def test_create_category_duplicate(client: TestClient, auth_headers: dict):
    payload = {"name": "Notebook Test"}
    response = client.post("/api/v1/categories/", json=payload, headers=auth_headers)
    assert response.status_code == 409


def test_list_categories(client: TestClient, auth_headers: dict):
    response = client.get("/api/v1/categories/", headers=auth_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_update_category(client: TestClient, auth_headers: dict):
    response = client.put(
        "/api/v1/categories/1",
        json={"description": "Nova descrição"},
        headers=auth_headers,
    )
    assert response.status_code == 200


def test_delete_category(client: TestClient, auth_headers: dict):
    payload = {"name": "Para Deletar"}
    create = client.post("/api/v1/categories/", json=payload, headers=auth_headers)
    cat_id = create.json()["id"]
    response = client.delete(f"/api/v1/categories/{cat_id}", headers=auth_headers)
    assert response.status_code == 200
