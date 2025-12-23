from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict


class TaskBase(BaseModel):
    """
    Base schema with common task attributes.
    Other schemas inherit from this to avoid repetition.
    """
    task_name: str = Field(
        min_length=1, 
        max_length=100,
        examples=["Clean my room"]
    )
    description: str = Field(
        min_length=1, 
        max_length=500,
        examples=["Vacuum the floor and dust the shelves"]
    )


class TaskCreate(TaskBase):
    """
    Schema for creating a new task.
    
    Only requires task_name and description.
    id, completed, created_at are set automatically.
    """
    pass  # Inherits everything from TaskBase


class TaskUpdate(BaseModel):
    """
    Schema for updating a task.
    
    All fields are optional - only update what's provided.
    """
    task_name: str | None = Field(
        default=None, 
        min_length=1, 
        max_length=100
    )
    description: str | None = Field(
        default=None, 
        min_length=1, 
        max_length=500
    )
    completed: bool | None = None


class TaskResponse(TaskBase):
    """
    Schema for task responses (what we send back to users).
    
    Includes all fields including auto-generated ones.
    """
    id: int
    completed: bool
    created_at: datetime
    
    # This tells Pydantic to read data from ORM models (SQLAlchemy)
    model_config = ConfigDict(from_attributes=True)


class TaskComplete(BaseModel):
    """
    Schema specifically for marking a task complete.
    """
    completed: bool = True