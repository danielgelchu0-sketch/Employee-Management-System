from app.queries.employee_queries import get_employees_with_departments


employees = get_employees_with_departments()

for employee in employees:
    print(
        employee.first_name,
        employee.last_name,
        "-",
        employee.department.name
    )