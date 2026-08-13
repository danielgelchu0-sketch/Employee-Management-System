from app.database.database import SessionLocal
from app.database.models import Department


session = SessionLocal()

department = (
    session.query(Department)
    .filter(Department.name == "Information Technology")
    .first()
)

print("Department:")
print("ID:", department.id)
print("Name:", department.name)
print("Location:", department.location)

session.close()