from pydantic import BaseModel
from datetime import datetime

# My input schema for creating or updating todos

# ---- TODO SCHEMA ----
class TodoBase(BaseModel):
    title: str
    description: str | None = None
    is_complete: bool | None = None
    due_date: datetime | None = None


class TodoCreate(TodoBase):
    is_complete: bool = False


class TodoUpdate(TodoBase):
    title: str | None = None
    description: str | None = None
    is_complete: bool | None = None
    due_date: datetime | None = None


# ---- SUBTASKS SCHEMA ----
class SubtaskBase(BaseModel):
    title: str
    is_complete: bool = False

class SubtaskCreate(SubtaskBase):
    pass

class SubtaskUpdate(SubtaskBase):
    title: str | None = None
    is_complete: bool | None = None

class SubtaskResponse(SubtaskBase):
    id: int
    todo_id: int

    model_config = {
        "from_attributes": True
    }


class TodoResponse(TodoBase):
    id: int
    created_at: datetime
    updated_at: datetime | None = None
    subtasks: list[SubtaskResponse] = []

    model_config = {
        "from_attributes": True
    }
