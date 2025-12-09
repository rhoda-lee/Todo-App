from pydantic import BaseModel
from datetime import datetime

# My input schema for creating or updating todos

class TodoCreate(BaseModel):
    title: str
    description: str

class TodoResponse(BaseModel):
    id: int
    title: str
    description: str
    created_at: datetime
    updated_at: datetime


model_config = {
    "from_attributes": True
}
