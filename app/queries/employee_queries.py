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

def get_employees_filtered(department_name=None, min_salary=None, max_salary=None, sort_by="last_name"):
    session = SessionLocal()

    query = (
        session.query(Employee)
        .options(joinedload(Employee.department))
    )

    if department_name:
        query = query.join(Employee.department).filter(Department.name == department_name)

    if min_salary is not None:
        query = query.filter(Employee.salary >= min_salary)

    if max_salary is not None:
        query = query.filter(Employee.salary <= max_salary)

    sort_columns = {
        "last_name": Employee.last_name,
        "salary": Employee.salary,
        "hire_date": Employee.hire_date,
    }
    query = query.order_by(sort_columns.get(sort_by, Employee.last_name))

    employees = query.all()

    session.close()

    return employees


def get_employees_filtered_raw(department_name=None, min_salary=None, max_salary=None, sort_by="last_name"):
    session = SessionLocal()

    conditions = []
    params = {}

    if department_name:
        conditions.append("d.name = :department_name")
        params["department_name"] = department_name

    if min_salary is not None:
        conditions.append("e.salary >= :min_salary")
        params["min_salary"] = min_salary

    if max_salary is not None:
        conditions.append("e.salary <= :max_salary")
        params["max_salary"] = max_salary

    where_clause = ("WHERE " + " AND ".join(conditions)) if conditions else ""

    allowed_sort_columns = {
        "last_name": "e.last_name",
        "salary": "e.salary",
        "hire_date": "e.hire_date",
    }
    sort_column = allowed_sort_columns.get(sort_by, "e.last_name")

    sql = text(f"""
        SELECT
            e.id,
            e.first_name,
            e.last_name,
            e.salary,
            d.name AS department_name
        FROM employees AS e
        JOIN departments AS d
            ON d.id = e.department_id
        {where_clause}
        ORDER BY {sort_column}
    """)

    result = session.execute(sql, params)
    employees = result.mappings().all()

    session.close()

    return employees