from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import schemas, crud

router = APIRouter(prefix="/attendance")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def mark_attendance(data: schemas.AttendanceCreate, db: Session = Depends(get_db)):
    return crud.mark_attendance(db, data)


@router.get("/{employee_id}")
def get_attendance(employee_id: int, db: Session = Depends(get_db)):
    return crud.get_attendance_by_employee(db, employee_id)