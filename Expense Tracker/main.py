from fastapi import FastAPI , Depends
from sqlalchemy.orm import Session
import models, schemas, crud
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app=FastAPI()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/expenses")
def add_expense(expense: schemas.ExpenseCreate , db: Session = Depends(get_db)):
    return crud.add_expense(db, expense)

@app.get("/expenses")
def get_expenses(category:str | None = None , db: Session = Depends(get_db)):
    return crud.get_expenses(db, expense)

@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int, db:Session = Depends(get_db)):
    return crud.delete_expense(db, expense_id)

@app.get("/expenses/total")
def total_expense(db: Session = Depends(get_db)):
    return {"total": crud.total_expense(db)}


