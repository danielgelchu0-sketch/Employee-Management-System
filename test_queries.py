from sqlalchemy import text

from app.database.database import SessionLocal
from app.database.models import Department


session = SessionLocal()


# ORM query
department = (
    session.query(Department)
    .filter(Department.name == "Information Technology")
    .first()
)

print("ORM:")
print("ID:", department.id)
print("Name:", department.name)
print("Location:", department.location)


# Raw SQL query
result = session.execute(
    text("""
        SELECT id, name, location
        FROM departments
        WHERE name = :department_name
    """),
    {"department_name": "Information Technology"}
)

department_row = result.fetchone()

print("\nRaw SQL:")
print("ID:", department_row.id)
print("Name:", department_row.name)
print("Location:", department_row.location)


session.close()