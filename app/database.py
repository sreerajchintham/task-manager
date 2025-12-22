from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from app.config import get_settings

settings = get_settings()

engine = create_engine(
    settings.database_url,
    connect_args={"check_same_thread": False}  # Needed for SQLite only
)
# Create a session factory
# Sessions are how you interact with the database (query, add, delete)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    """
    All database models will inherit from this class.
    This is how SQLAlchemy knows what tables to create.
    """
    pass

def get_db():
    """
    Dependency that provides a database session.
    Used in FastAPI routes to get database access.
    
    Yields a session, then closes it when done.
    This pattern ensures connections don't leak.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()