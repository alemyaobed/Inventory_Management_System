from fastapi import FastAPI
from app.api import api_router
from app.database import Base, engine

# Initialize FastAPI app
app = FastAPI(
    title="Inventory Management System",
    description="API for managing products, suppliers, and orders",
    version="1.0.0",
)

# Create database tables if they don't exist
Base.metadata.create_all(bind=engine)

# Include the API routes
app.include_router(api_router)
