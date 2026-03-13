import os
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

def get_db_password():
    password_file = os.getenv("POSTGRES_PASSWORD_FILE")
    if password_file and os.path.exists(password_file):
        with open(password_file, "r") as f:
            return f.read().strip()
    return os.getenv("POSTGRES_PASSWORD", "supersafe")

password = get_db_password()
# Use password in DATABASE_URL logic...

class Todo(BaseModel):
    id: int
    task: str
    completed: bool = False

todos = []

@app.get("/")
def read_root():
    return {"message": "Welcome to the Todo API"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/todos", response_model=List[Todo])
def get_todos():
    return todos

@app.post("/todos", response_model=Todo)
def create_todo(todo: Todo):
    todos.append(todo)
    return todo
