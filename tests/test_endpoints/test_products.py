import pytest
from fastapi.testclient import TestClient
from app.main import app
from app import crud, models, schemas
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

client = TestClient(app)

@pytest.fixture(scope="module")
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_create_product_endpoint(setup_db):
    response = client.post("/products/", json={"name": "New Product", "description": "A new product", "price": 25.50, "quantity": 100})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "New Product"
    assert data["description"] == "A new product"
    assert data["price"] == 25.50
    assert data["quantity"] == 100

def test_read_product_endpoint(setup_db):
    response = client.post("/products/", json={"name": "Another Product", "description": "Another product", "price": 30.00, "quantity": 50})
    assert response.status_code == 200
    created_product_id = response.json()["id"]

    response = client.get(f"/products/{created_product_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Another Product"
    assert data["description"] == "Another product"
    assert data["price"] == 30.00
    assert data["quantity"] == 50
