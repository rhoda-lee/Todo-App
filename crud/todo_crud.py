from sqlalchemy import select, asc, nulls_last
from sqlalchemy.orm import Session
from models.todo_model import Todo, Subtask
from schema.todo_schema import TodoCreate, TodoUpdate, SubtaskCreate, SubtaskUpdate


class TodoCrud:

    @staticmethod
    def create_todo(db: Session, todo_data: TodoCreate) -> Todo:
        """Create a new todo item"""
        todo = Todo(**todo_data.model_dump())
        db.add(todo)
        db.commit()
        db.refresh(todo)
        return todo

    @staticmethod
    def get_all_todos(db: Session) -> list[Todo]:
        result = db.execute(select(Todo).order_by(
            nulls_last(asc(Todo.due_date))))
        return result.scalars().all()

    @staticmethod
    def get_todo_by_id(db: Session, todo_id: int) -> Todo | None:
        """Update a todo item"""
        result = db.execute(select(Todo).where(Todo.id == todo_id))
        return result.scalar_one_or_none()

    @staticmethod
    def update_todo(db: Session, todo_id: int, todo_data: TodoUpdate) -> Todo | None:
        """Update a todo item"""
        result = db.execute(select(Todo).where(Todo.id == todo_id))
        todo = result.scalar_one_or_none()

        if not todo:
            return None
        update_data = todo_data.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(todo, key, value)
        db.commit()
        db.refresh(todo)
        return todo

    @staticmethod
    def delete_todo(db: Session, todo_id: int) -> bool:
        """Delete a todo item"""
        result = db.execute(select(Todo).where(Todo.id == todo_id))
        todo = result.scalar_one_or_none()

        if not todo:
            return None
        db.delete(todo)
        db.commit()
        return f'Todo item with id: {todo_id} has been deleted'
    
    # ---- SUBTASKS CRUD ----
    @staticmethod
    def create_subtask(db: Session, todo_id: int, subtask_data: SubtaskCreate) -> Subtask | None:
        # checking for parent todo item
        todo = db.get(Todo, todo_id)
        if not todo:
            return None
        
        # creating subtask
        subtask = Subtask(**subtask_data.model_dump(), todo_id = todo_id)
        db.add(subtask)
        db.commit()
        db.refresh(subtask)

        # logic: if subtaks is marked completed, should not mark parent task as completed
        if  not subtask.is_complete and todo.is_complete:
            todo.is_complete = False
            db.commit

        return subtask

