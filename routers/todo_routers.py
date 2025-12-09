from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.connection import session
from schema.todo_schema import TodoCreate, TodoResponse
from crud.todo_crud import TodoCrud

router = APIRouter(prefix='/todos', tags=['Todos'])

# Session dependency (DB)


def get_db():
    db = session()

    try:
        yield db
    finally:
        db.close()


"""API Routes"""

# Create a Todo Item


@router.post('/', response_model=TodoResponse)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    return TodoCrud.create_todo(db, todo)

# Get all todo items


@router.get('/', response_model=list[TodoResponse])
def get_all_todos(db: Session = Depends(get_db)):
    todos = TodoCrud.get_all_todos(db)
    return [
        TodoResponse.model_validate({
            "id": todo.id,
            "title": todo.title,
            "description": todo.description,
            "created_at": todo.created_at,
            "updated_at": todo.updated_at,
        })
        for todo in todos
    ]

# Get todo by ID


@router.get('/{todo_id}', response_model=TodoResponse)
def get_todo_by_id(todo_id: int, db: Session = Depends(get_db)):
    todo = TodoCrud.get_todo_by_id(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail='Todo not found')
    return todo

# Update a todo item


@router.put('/{todo_id}', response_model=TodoResponse)
def update_todo(todo_id: int, todo: TodoCreate, db: Session = Depends(get_db)):
    updated = TodoCrud.update_todo(db, todo_id, todo)
    if not updated:
        raise HTTPException(status_code=404, detail='Todo not found')
    return updated

# Delete a todo item


@router.delete('/{todo_id}')
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    deleted = TodoCrud.delete_todo(db, todo_id)
    if not deleted:
        raise HTTPException(status_code=404, detail='Todo not Found')
    return deleted
