def get_employees_filtered(department_name=None, min_salary=None, max_salary=None, sort_by="last_name"):
    session = SessionLocal()

    query = (
        session.query(Employee)
        .join(Employee.department)
        .options(contains_eager(Employee.department))
    )

    if department_name:
        query = query.filter(Department.name == department_name)

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