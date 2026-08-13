from app.database.database import SessionLocal
from app.database.models import Employee


session = SessionLocal()

employee = session.query(Employee).filter(Employee.id == 3).first()

if employee:
    print("Employee:", employee.first_name, employee.last_name)
    print("Department:", employee.department.name)
    print("Location:", employee.department.location)

session.close()