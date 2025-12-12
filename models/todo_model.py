from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, DateTime, func, Boolean, ForeignKey
from database.connection import Base, session, engine


class Todo(Base):
    __tablename__ = "todos"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str | None] = mapped_column(String, nullable=True)
    is_complete: Mapped[bool] = mapped_column(Boolean, default=False)
    due_date: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        onupdate=func.now(),
        server_default=func.now())

    # relationship
    subtasks: Mapped[list['Subtask']] = relationship(
        back_populates='todo', cascade='all, delete-orphan', lazy='selectin')


class Subtask(Base):
    __tablename__ = 'subtasks'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    is_complete: Mapped[bool] = mapped_column(Boolean, default=False)

    # foreign key
    todo_id: Mapped[int] = mapped_column(ForeignKey(Todo.id))

    # relationship
    todo: Mapped["Todo"] = relationship(back_populates='subtasks')

    # def __str__(self):
    #     return f"Todo ID: {self.id}, Title: {self.title}, Description: {self.description}, Created AT: {self.created_at}"

    # def __repr__(self):
    #     return f"A todo item has an ID = {self.id}, a Title = {self.title}, a Description = {self.description} and was Created = {self.created_at}"

    # def get_id(self):
    #     return str(self.id)
if __name__ == '__main__':
    try:
        Base.metadata.create_all(bind=engine)
        print('Tables created successfully!')
    except Exception as e:
        print(f'An error occured: {e}')
