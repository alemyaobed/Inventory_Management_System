from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.api.endpoints import products, suppliers, orders
from app.database import Base, engine
# from app.tasks import create_background_tasks

# Initialize FastAPI app
app = FastAPI(
    title="Inventory Management System",
    description="API for managing products, suppliers, and orders in the Inventory Management System",
    version="1.0.0"
)

# Set up CORS (Cross-Origin Resource Sharing)
origins = [
    "http://localhost",
    "http://localhost:8000",
    # Add production URL here
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables
Base.metadata.create_all(bind=engine)

# Include routers for API endpoints
app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(suppliers.router, prefix="/suppliers", tags=["Suppliers"])
app.include_router(orders.router, prefix="/orders", tags=["Orders"])

# # Background tasks (optional, Celery)
# @app.on_event("startup")
# async def startup_event():
#     create_background_tasks()

# Health check endpoint
@app.get("/", tags=["Health"])
def health_check():
    return {"status": "Healthy", "message": "API is running!"}
