from sqlalchemy.orm import Session
from . import models, schemas


def create_employee(db: Session, employee: schemas.EmployeeCreate):

    existing_employee = db.query(models.Employee).filter(
        models.Employee.employee_id == employee.employee_id
    ).first()

    if existing_employee:
        raise ValueError("Employee ID already exists")

    db_employee = models.Employee(**employee.dict())

    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)

    return db_employee


def get_employees(db: Session):
    return db.query(models.Employee).all()


def delete_employee(db: Session, employee_id: int):

    emp = db.query(models.Employee).filter(models.Employee.id == employee_id).first()

    if not emp:
        return None

    db.delete(emp)
    db.commit()

    return emp


def mark_attendance(db: Session, attendance: schemas.AttendanceCreate):

    db_att = models.Attendance(**attendance.dict())

    db.add(db_att)
    db.commit()
    db.refresh(db_att)

    return db_att


def get_attendance_by_employee(db: Session, employee_id: int):

    return db.query(models.Attendance).filter(
        models.Attendance.employee_id == employee_id
    ).all()