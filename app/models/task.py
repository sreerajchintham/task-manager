from datetime import datetime
from sqlalchemy import Integer, String, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from app.database import Base

from datetime import datetime
from sqlalchemy import Integer, String, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from app.database import Base


class Task(Base):
    """
    Database model for tasks.
    
    This class defines the 'tasks' table structure.
    Each attribute with mapped_column becomes a column in the database.
    """
    
    __tablename__ = "tasks"
    
    # Primary key - auto-generated unique identifier
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    
    # Task content
    task_name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    
    # Status
    completed: Mapped[bool] = mapped_column(Boolean, default=False)
    
    # Timestamps - automatically set
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), 
        server_default=func.now()
    )
    
    def __repr__(self) -> str:
        """How the object looks when printed (for debugging)."""
        return f"<Task(id={self.id}, name='{self.task_name}', completed={self.completed})>"