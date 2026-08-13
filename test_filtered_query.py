from app.queries.employee_queries import get_employees_filtered, get_employees_filtered_raw

print("ORM version:")
for e in get_employees_filtered(department_name="Information Technology", min_salary=20000, sort_by="salary"):
    print(e.first_name, e.last_name, e.salary, e.department.name)

print("\nRaw SQL version:")
for e in get_employees_filtered_raw(department_name="Information Technology", min_salary=20000, sort_by="salary"):
    print(e["first_name"], e["last_name"], e["salary"], e["department_name"])
