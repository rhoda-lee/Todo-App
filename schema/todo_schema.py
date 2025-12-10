from pydantic import BaseModel
from datetime import datetime

# My input schema for creating or updating todos


class TodoBase(BaseModel):
    title: str
    description: str | None = None
    is_complete: bool | None = None


class TodoCreate(TodoBase):
    is_complete: bool = False


class TodoUpdate(TodoBase):
    title: str | None = None
    description: str | None = None
    is_complete: bool | None = None


class TodoResponse(TodoBase):
    id: int
    created_at: datetime
    updated_at: datetime | None = None

    model_config = {
        "from_attributes": True
    }
