from fastapi import FastAPI, Depends
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from database import TodoItem

from database import SessionLocal

app = FastAPI()


# add auto incrementing feature

class requirements(BaseModel):
    title: str = Field(max_length=400)
    description: str = Field(max_length=400)
    difficulty: int = Field(gt=0, lt=6, default=1)
    importance: int = Field(gt=0, lt=6, default=1)
    completed: bool = False


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# It works!

@app.post("/todo")
async def create_data(request: requirements, db: Session = Depends(get_db)):
    # need to create a new instance to be able to add it to the database.
    todo_item = TodoItem(
        title=request.title,
        description=request.description,
        difficulty=request.difficulty,
        importance=request.importance,
        completed=request.completed
    )
    db.add(todo_item)
    db.commit()
    db.refresh(todo_item)
    return {"message": f"Todo item created successfully        {request}"}


@app.get("/todo")
async def read_data(db: Session = Depends(get_db)):
    todos = db.query(TodoItem).all()
    return todos


@app.delete("/todo/{item_id}")
async def delete_data(item_id: int, db: Session = Depends(get_db)):
    item_to_delete = db.query(TodoItem).filter(TodoItem.id == item_id).first()  # added .first and forot TodoItem.id
    if item_to_delete:
        db.delete(item_to_delete)
        db.commit()
        return {"message": "Item was successfully deleted"}
    return {"Error": "Item id does not exist"}
