from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

# Schemas for Product
class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    quantity: int

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    orders: List[int] = []

    class Config:
        orm_mode = True

# Schemas for Supplier
class SupplierBase(BaseModel):
    name: str
    contact_info: str

class SupplierCreate(SupplierBase):
    pass

class Supplier(SupplierBase):
    id: int
    orders: List[int] = []

    class Config:
        orm_mode = True

# Schemas for Order
class OrderBase(BaseModel):
    product_id: int
    supplier_id: int
    quantity_ordered: int

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int
    order_date: datetime

    class Config:
        orm_mode = True
