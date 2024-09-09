import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_supplier_endpoint():
    response = client.post("/suppliers/", json={"name": "Supplier One", "contact_info": "contact@supplierone.com"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Supplier One"
    assert data["contact_info"] == "contact@supplierone.com"

def test_read_supplier_endpoint():
    response = client.post("/suppliers/", json={"name": "Supplier Two", "contact_info": "contact@suppliertwo.com"})
    assert response.status_code == 200
    created_supplier_id = response.json()["id"]

    response = client.get(f"/suppliers/{created_supplier_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Supplier Two"
    assert data["contact_info"] == "contact@suppliertwo.com"
