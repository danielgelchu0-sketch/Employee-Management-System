from app.queries.employee_queries import get_department_salary_summary, get_department_salary_summary_raw

print("ORM version:")
for row in get_department_salary_summary():
    print(row.name, "-", row.employee_count, "employees, avg:", row.average_salary, "total:", row.total_salary)

print("\nRaw SQL version:")
for row in get_department_salary_summary_raw():
    print(row["department_name"], "-", row["employee_count"], "employees, avg:", row["average_salary"], "total:", row["total_salary"])
