from app.database.database import SessionLocal
from app.database.models import Employee


def get_all_employees():
    session = SessionLocal()

    employees = session.query(Employee).all()

    session.close()

    return employees