# Employee Management System
import math
from functools import reduce

employees = []
def add_employee():
    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    salary = float(input("Enter Salary: "))

    employee = {
        "id": emp_id,
        "name": name,
        "salary": salary
    }

    employees.append(employee)

    print("Employee Added Successfully")

def display_employees():

    if len(employees) == 0:
        print("No Employees Found")

    else:
        print("\nEmployee Records")

        for emp in employees:
            print(emp)

def calculate_bonus():

    if len(employees) == 0:
        print("No Employees Found")
        return

    print("\nBonus Details")

    for emp in employees:

        bonus = math.sqrt(emp["salary"]) * 100

        print(emp["name"], "Bonus =", round(bonus, 2))

def salary_increment():

    global employees

    employees = list(map(
        lambda emp: {
            "id": emp["id"],
            "name": emp["name"],
            "salary": emp["salary"] + 5000
        },
        employees
    ))

    print("Salary Increment Applied")

def high_salary_employees():

    high_salary = list(filter(
        lambda emp: emp["salary"] > 50000,
        employees
    ))

    print("\nEmployees with Salary > 50000")

    for emp in high_salary:
        print(emp)

def total_salary():

    if len(employees) == 0:
        print("No Employees Found")
        return

    total = reduce(
        lambda x, y: x + y["salary"],
        employees,
        0
    )

    print("Total Salary =", total)

def company_info():

    info = ("ABC Technologies", "Hyderabad", 2026)

    print("\nCompany Name :", info[0])
    print("Location     :", info[1])
    print("Established  :", info[2])

while True:

    print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Calculate Bonus")
    print("4. Salary Increment")
    print("5. High Salary Employees")
    print("6. Total Salary")
    print("7. Company Info")
    print("8. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        add_employee()

    elif choice == 2:
        display_employees()

    elif choice == 3:
        calculate_bonus()

    elif choice == 4:
        salary_increment()

    elif choice == 5:
        high_salary_employees()

    elif choice == 6:
        total_salary()

    elif choice == 7:
        company_info()

    elif choice == 8:
        print("Program Closed")
        break

    else:
        print("Invalid Choice")