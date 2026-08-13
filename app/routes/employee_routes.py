from flask import Blueprint, jsonify, request

from app.queries.employee_queries import (
    get_all_employees,
    get_employee_by_id,
    get_employees_with_departments,
    get_employees_with_departments_raw,
    get_employees_filtered,
    get_employees_filtered_raw,
    get_department_salary_summary,
    get_department_salary_summary_raw,
)

employee_routes = Blueprint("employee_routes", __name__)


def employee_to_dict(employee):
    return {
        "id": employee.id,
        "first_name": employee.first_name,
        "last_name": employee.last_name,
        "email": employee.email,
        "phone": employee.phone,
        "salary": float(employee.salary),
        "hire_date": employee.hire_date.isoformat(),
        "department": employee.department.name if employee.department else None,
    }


@employee_routes.route("/api/employees", methods=["GET"])
def list_employees():
    employees = get_all_employees()
    return jsonify([
        {
            "id": e.id,
            "first_name": e.first_name,
            "last_name": e.last_name,
            "email": e.email,
            "salary": float(e.salary),
        }
        for e in employees
    ])


@employee_routes.route("/api/employees/<int:employee_id>", methods=["GET"])
def get_employee(employee_id):
    employee = get_employee_by_id(employee_id)
    if employee is None:
        return jsonify({"error": "Employee not found"}), 404
    return jsonify({
        "id": employee.id,
        "first_name": employee.first_name,
        "last_name": employee.last_name,
        "email": employee.email,
        "salary": float(employee.salary),
    })


@employee_routes.route("/api/employees/with-departments", methods=["GET"])
def list_employees_with_departments():
    employees = get_employees_with_departments()
    return jsonify([employee_to_dict(e) for e in employees])


@employee_routes.route("/api/employees/with-departments/raw", methods=["GET"])
def list_employees_with_departments_raw():
    employees = get_employees_with_departments_raw()
    return jsonify([dict(e) for e in employees])


@employee_routes.route("/api/employees/filtered", methods=["GET"])
def list_employees_filtered():
    department_name = request.args.get("department")
    min_salary = request.args.get("min_salary", type=float)
    max_salary = request.args.get("max_salary", type=float)
    sort_by = request.args.get("sort_by", default="last_name")

    employees = get_employees_filtered(
        department_name=department_name,
        min_salary=min_salary,
        max_salary=max_salary,
        sort_by=sort_by,
    )
    return jsonify([employee_to_dict(e) for e in employees])


@employee_routes.route("/api/employees/filtered/raw", methods=["GET"])
def list_employees_filtered_raw():
    department_name = request.args.get("department")
    min_salary = request.args.get("min_salary", type=float)
    max_salary = request.args.get("max_salary", type=float)
    sort_by = request.args.get("sort_by", default="last_name")

    employees = get_employees_filtered_raw(
        department_name=department_name,
        min_salary=min_salary,
        max_salary=max_salary,
        sort_by=sort_by,
    )
    return jsonify([dict(e) for e in employees])


@employee_routes.route("/api/departments/summary", methods=["GET"])
def department_summary():
    rows = get_department_salary_summary()
    return jsonify([
        {
            "department": row.name,
            "employee_count": row.employee_count,
            "average_salary": float(row.average_salary),
            "total_salary": float(row.total_salary),
        }
        for row in rows
    ])


@employee_routes.route("/api/departments/summary/raw", methods=["GET"])
def department_summary_raw():
    rows = get_department_salary_summary_raw()
    return jsonify([
        {
            "department": row["department_name"],
            "employee_count": row["employee_count"],
            "average_salary": float(row["average_salary"]),
            "total_salary": float(row["total_salary"]),
        }
        for row in rows
    ])