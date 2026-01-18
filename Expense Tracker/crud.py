from sqlalchemy.orm import Session
import models, schemas
from sqlalchemy import func

def add_expense(db: Session, expense: schemas.ExpenseCreate):
    db_expense = models.Expense(
        title=expense.title,
        amount=expense.amount,
        category=expense.category,
        date=expense.date
    )
    db.add(db_expense)
    db.commit()
    db.refresh()
    return db_expense

def get_expenses(db: Session, category: str | None = None):
    query = db.query(models.Expense)
    if category:
        query = query.filter(models.Expense.category==category)
    return query.all()
    
def delete_expense(db: Session,expense_id: int):
    expense=db.query(models.Expense).filter(models.Expense.id == expense_id).first()
    if expense:
        db.delete(expense)
        db.commit()
    
    return expense




def total_expense(db: Session):
    total=db.query(func.sum(models.Expense.amount)).scalar()
    return total if total else 0