from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config import get_settings
from app.database import engine, Base
from app.routers import tasks_router


# Get settings
settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan context manager for startup and shutdown events.
    
    - Startup: Create database tables
    - Shutdown: Cleanup (if needed)
    """
    # Startup: Create all tables defined in models
    Base.metadata.create_all(bind=engine)
    print("✅ Database tables created")
    
    yield  # App runs here
    
    # Shutdown: Cleanup (optional)
    print("👋 Shutting down...")


# Create FastAPI application
app = FastAPI(
    title=settings.app_name,
    description="A RESTful API for managing tasks",
    version="1.0.0",
    lifespan=lifespan,
)


# Include routers
app.include_router(tasks_router)


# Root endpoint
@app.get("/")
def root():
    """
    Root endpoint - health check.
    """
    return {
        "message": "Welcome to Task Manager API",
        "docs": "/docs",
        "health": "ok"
    }


@app.get("/health")
def health_check():
    """
    Health check endpoint for monitoring.
    """
    return {"status": "healthy"}