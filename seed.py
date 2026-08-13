from datetime import date

from app.database.database import SessionLocal
from app.database.models import (
    Department,
    Position,
    Employee,
    Project,
    EmployeeProject,
)


session = SessionLocal()


# Departments
departments = [
    Department(name="Information Technology", location="Building A"),
    Department(name="Human Resources", location="Building B"),
    Department(name="Finance", location="Building C"),
    Department(name="Marketing", location="Building A"),
    Department(name="Operations", location="Building D"),
]


# Positions
positions = [
    Position(title="Software Engineer", level="Junior"),
    Position(title="Senior Software Engineer", level="Senior"),
    Position(title="Database Administrator", level="Senior"),
    Position(title="HR Specialist", level="Mid"),
    Position(title="Accountant", level="Mid"),
    Position(title="Project Manager", level="Senior"),
]


session.add_all(departments)
session.add_all(positions)
session.commit()


# Employees
employees = [
    Employee(
        first_name="Abebe",
        last_name="Kebede",
        email="abebe@example.com",
        phone="0911000001",
        salary=25000,
        hire_date=date(2025, 1, 15),
        department_id=1,
        position_id=1,
    ),
    Employee(
        first_name="Sara",
        last_name="Ahmed",
        email="sara@example.com",
        phone="0911000002",
        salary=35000,
        hire_date=date(2024, 6, 10),
        department_id=1,
        position_id=2,
    ),
    Employee(
        first_name="Dawit",
        last_name="Tesfaye",
        email="dawit@example.com",
        phone="0911000003",
        salary=32000,
        hire_date=date(2024, 3, 20),
        department_id=1,
        position_id=3,
    ),
    Employee(
        first_name="Hana",
        last_name="Bekele",
        email="hana@example.com",
        phone="0911000004",
        salary=22000,
        hire_date=date(2025, 2, 5),
        department_id=2,
        position_id=4,
    ),
    Employee(
        first_name="Mekdes",
        last_name="Worku",
        email="mekdes@example.com",
        phone="0911000005",
        salary=28000,
        hire_date=date(2023, 9, 12),
        department_id=3,
        position_id=5,
    ),
    Employee(
        first_name="Yonas",
        last_name="Girma",
        email="yonas@example.com",
        phone="0911000006",
        salary=30000,
        hire_date=date(2024, 11, 1),
        department_id=3,
        position_id=6,
    ),
    Employee(
        first_name="Liya",
        last_name="Tadesse",
        email="liya@example.com",
        phone="0911000007",
        salary=24000,
        hire_date=date(2025, 4, 18),
        department_id=4,
        position_id=1,
    ),
    Employee(
        first_name="Samuel",
        last_name="Alemu",
        email="samuel@example.com",
        phone="0911000008",
        salary=27000,
        hire_date=date(2024, 8, 25),
        department_id=5,
        position_id=6,
    ),
]


session.add_all(employees)
session.commit()


# Projects
projects = [
    Project(
        name="Employee Management System",
        budget=150000,
        start_date=date(2026, 1, 10),
        end_date=date(2026, 6, 30),
    ),
    Project(
        name="Hospital Management System",
        budget=300000,
        start_date=date(2026, 2, 15),
        end_date=date(2026, 12, 30),
    ),
    Project(
        name="Banking Application",
        budget=500000,
        start_date=date(2026, 3, 1),
        end_date=None,
    ),
    Project(
        name="Marketing Analytics Platform",
        budget=200000,
        start_date=date(2026, 4, 1),
        end_date=date(2026, 10, 31),
    ),
]


session.add_all(projects)
session.commit()


# Employee-project assignments
assignments = [
    EmployeeProject(
        employee_id=1,
        project_id=1,
        assigned_date=date(2026, 1, 15),
        role="Backend Developer",
    ),
    EmployeeProject(
        employee_id=2,
        project_id=1,
        assigned_date=date(2026, 1, 15),
        role="Team Lead",
    ),
    EmployeeProject(
        employee_id=3,
        project_id=1,
        assigned_date=date(2026, 1, 20),
        role="Database Administrator",
    ),
    EmployeeProject(
        employee_id=1,
        project_id=2,
        assigned_date=date(2026, 2, 20),
        role="Backend Developer",
    ),
    EmployeeProject(
        employee_id=2,
        project_id=2,
        assigned_date=date(2026, 2, 20),
        role="Technical Lead",
    ),
    EmployeeProject(
        employee_id=6,
        project_id=2,
        assigned_date=date(2026, 2, 25),
        role="Project Manager",
    ),
    EmployeeProject(
        employee_id=2,
        project_id=3,
        assigned_date=date(2026, 3, 10),
        role="Technical Lead",
    ),
    EmployeeProject(
        employee_id=7,
        project_id=4,
        assigned_date=date(2026, 4, 5),
        role="Developer",
    ),
    EmployeeProject(
        employee_id=8,
        project_id=4,
        assigned_date=date(2026, 4, 5),
        role="Project Manager",
    ),
]


session.add_all(assignments)
session.commit()

print("Seed data inserted successfully.")

session.close()