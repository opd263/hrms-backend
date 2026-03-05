from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import schemas, crud

router = APIRouter(prefix="/employees")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_employee(db, employee)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/")
def get_employees(db: Session = Depends(get_db)):
    return crud.get_employees(db)


@router.delete("/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db)):

    emp = crud.delete_employee(db, employee_id)

    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")

    return {"message": "Employee deleted"}