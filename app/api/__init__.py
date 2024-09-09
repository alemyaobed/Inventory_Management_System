from fastapi import APIRouter

from .endpoints import products, suppliers, orders

# Create a master router for the API
api_router = APIRouter()

# Include individual routers
api_router.include_router(products.router, prefix="/products", tags=["products"])
api_router.include_router(suppliers.router, prefix="/suppliers", tags=["suppliers"])
api_router.include_router(orders.router, prefix="/orders", tags=["orders"])
