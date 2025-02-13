from flask import Flask, render_template, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

# Sample employee data (would be from a database in real implementation)
employees = [
    {"id": 1, "name": "John Doe", "attendance": 7},
    {"id": 2, "name": "Jane Smith", "attendance": 6},
    {"id": 3, "name": "Alice Brown", "attendance": 4},
    {"id": 4, "name": "Bob Johnson", "attendance": 2},
]

# Function to determine status based on attendance
def calculate_status(attendance):
    if attendance == 7:
        return "Excellent"
    elif 5 <= attendance <= 6:
        return "Good"
    elif 3 <= attendance <= 4:
        return "Average"
    elif 1 <= attendance <= 2:
        return "Bad"
    else:
        return "Very Poor"

@app.route("/")
def dashboard():
    for employee in employees:
        employee["status"] = calculate_status(employee["attendance"])
    return render_template("dashboard.html", employees=employees)

@app.route("/suspend_employee/<int:employee_id>")
def suspend_employee(employee_id):
    employee = next((e for e in employees if e["id"] == employee_id), None)
    if employee:
        employees.remove(employee)  # Simulating suspension by removing from list
        return jsonify({"message": f"Employee {employee['name']} suspended!"})
    return jsonify({"message": "Employee not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
