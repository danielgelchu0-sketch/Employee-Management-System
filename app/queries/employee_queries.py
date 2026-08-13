from sqlalchemy.orm import joinedload

from app.database.database import SessionLocal
from app.database.models import Employee


def get_all_employees():
    session = SessionLocal()

    employees = session.query(Employee).all()

    session.close()

    return employees


def get_employee_by_id(employee_id):
    session = SessionLocal()

    employee = (
        session.query(Employee)
        .filter(Employee.id == employee_id)
        .first()
    )

    session.close()

    return employee

def get_employees_with_departments():
    session = SessionLocal()

    employees = (
        session.query(Employee)
        .options(joinedload(Employee.department))
        .all()
    )

    session.close()

    return employees