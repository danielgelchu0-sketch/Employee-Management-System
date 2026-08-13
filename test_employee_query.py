from app.queries.employee_queries import get_employee_by_id


employee = get_employee_by_id(3)

if employee:
    print("Employee found:")
    print("ID:", employee.id)
    print("Name:", employee.first_name, employee.last_name)
    print("Email:", employee.email)
else:
    print("Employee not found.")