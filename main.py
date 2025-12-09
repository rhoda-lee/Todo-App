from fastapi import FastAPI
from routers.todo_routers import router as todo_router
from database.connection import engine, Base

app = FastAPI(title="Todo App with FastAPI + SQLAlchemy + PostgreSQL")

app.include_router(todo_router)


@app.get("/") 
def home():
    return {"message": "Welcome to my Todo App"}

if __name__ == '__main__':
    app.run(debug=True)
