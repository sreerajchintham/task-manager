from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from app.config import get_settings

settings = get_settings()

# Create engine based on database type
if settings.database_url.startswith("sqlite"):
    # SQLite configuration
    engine = create_engine(
        settings.database_url,
        connect_args={"check_same_thread": False}
    )
else:
    # PostgreSQL configuration
    # pool_pre_ping: Check if connection is alive before using it
    # pool_recycle: Recycle connections after 300 seconds (5 min)
    # This prevents "SSL connection closed unexpectedly" errors
    engine = create_engine(
        settings.database_url,
        pool_pre_ping=True,
        pool_recycle=300,
    )

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    """Base class for all database models."""
    pass


def get_db():
    """
    Dependency that provides a database session.
    Yields a session, then closes it when done.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
