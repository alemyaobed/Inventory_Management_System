import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_order_endpoint():
    response = client.post("/orders/", json={"product_id": 1, "supplier_id": 1, "quantity_ordered": 10})
    assert response.status_code == 200
    data = response.json()
    assert data["product_id"] == 1
    assert data["supplier_id"] == 1
    assert data["quantity_ordered"] == 10

def test_read_order_endpoint():
    response = client.post("/orders/", json={"product_id": 1, "supplier_id": 1, "quantity_ordered": 15})
    assert response.status_code == 200
    created_order_id = response.json()["id"]

    response = client.get(f"/orders/{created_order_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["product_id"] == 1
    assert data["supplier_id"] == 1
    assert data["quantity_ordered"] == 15
