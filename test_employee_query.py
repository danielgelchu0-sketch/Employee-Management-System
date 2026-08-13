from app.queries.employee_queries import get_all_employees


employees = get_all_employees()

for employee in employees:
    print(
        employee.id,
        employee.first_name,
        employee.last_name,
        employee.email
    )