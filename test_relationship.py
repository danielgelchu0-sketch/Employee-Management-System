from app.database.database import SessionLocal
from app.database.models import Department


session = SessionLocal()

department = (
    session.query(Department)
    .filter(Department.id == 1)
    .first()
)

if department:
    print("Department:", department.name)

    print("Employees:")

    for employee in department.employees:
        print(
            employee.id,
            employee.first_name,
            employee.last_name
        )

session.close()