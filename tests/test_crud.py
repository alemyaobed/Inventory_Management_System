import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base, get_db
from app import crud, models, schemas

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture(scope="module")
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_create_product(setup_db):
    db = TestingSessionLocal()
    product_in = schemas.ProductCreate(name="Test Product", description="A product for testing", price=99.99, quantity=10)
    product = crud.create_product(db=db, product=product_in)

    assert product.name == "Test Product"
    assert product.description == "A product for testing"
    assert product.price == 99.99
    assert product.quantity == 10

def test_get_product(setup_db):
    db = TestingSessionLocal()
    product_in = schemas.ProductCreate(name="Test Product", description="A product for testing", price=99.99, quantity=10)
    created_product = crud.create_product(db=db, product=product_in)

    product = crud.get_product(db, product_id=created_product.id)
    assert product is not None
    assert product.name == "Test Product"
