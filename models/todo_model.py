from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, DateTime, func, Boolean
from database.connection import Base, session, engine


class Todo(Base):
    __tablename__ = "todos"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    is_complete: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), onupdate=func.now(), server_default=func.now())

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
