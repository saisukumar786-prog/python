# Employee Management System
import math
from functools import reduce

class Employee:

    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print("ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("---------------------")


employees = []


def add_employee():

    try:
        emp_id = int(input("Enter Employee ID: "))
        name = input("Enter Employee Name: ")
        salary = float(input("Enter Salary: "))

        emp = Employee(emp_id, name, salary)

        employees.append(emp)

        print("Employee Added Successfully")

    except ValueError:
        print("Invalid Input")


def display_employee():

    if len(employees) == 0:
        print("No Records Found")

    else:
        for emp in employees:
            emp.display()


def save_file():

    try:

        file = open("employee.txt", "w")

        for emp in employees:

            file.write(
                str(emp.emp_id) + "," +
                emp.name + "," +
                str(emp.salary) + "\n"
            )

        file.close()

        print("Data Saved Successfully")

    except Exception as e:
        print("Error:", e)


def read_file():

    try:

        file = open("employee.txt", "r")

        print("\nEmployee Records From File")

        for line in file:
            print(line.strip())

        file.close()

    except FileNotFoundError:
        print("File Not Found")


def salary_increment():

    global employees

    employees = list(
        map(
            lambda emp:
            Employee(
                emp.emp_id,
                emp.name,
                emp.salary + 5000
            ),
            employees
        )
    )

    print("Increment Applied")


def high_salary():

    result = list(
        filter(
            lambda emp: emp.salary > 50000,
            employees
        )
    )

    print("\nHigh Salary Employees")

    for emp in result:
        emp.display()


def total_salary():

    total = reduce(
        lambda x, y: x + y.salary,
        employees,
        0
    )

    print("Total Salary =", total)


def company_info():

    company = (
        "ABC Technologies",
        "Hyderabad",
        2026
    )

    print("Company Name:", company[0])
    print("Location:", company[1])
    print("Established:", company[2])


def employee_dictionary():

    d = {}

    for emp in employees:

        d[emp.emp_id] = {
            "Name": emp.name,
            "Salary": emp.salary
        }

    print("\nDictionary Data")

    for key, value in d.items():
        print(key, value)


def bonus():

    for emp in employees:

        bonus_amount = math.sqrt(emp.salary)

        print(
            emp.name,
            "Bonus =",
            round(bonus_amount, 2)
        )


while True:

    print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")

    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Save To File")
    print("4. Read From File")
    print("5. Salary Increment")
    print("6. High Salary Employees")
    print("7. Total Salary")
    print("8. Company Information")
    print("9. Dictionary View")
    print("10. Bonus Calculation")
    print("11. Exit")

    try:

        choice = int(input("Enter Choice: "))

        if choice == 1:
            add_employee()

        elif choice == 2:
            display_employee()

        elif choice == 3:
            save_file()

        elif choice == 4:
            read_file()

        elif choice == 5:
            salary_increment()

        elif choice == 6:
            high_salary()

        elif choice == 7:
            total_salary()

        elif choice == 8:
            company_info()

        elif choice == 9:
            employee_dictionary()

        elif choice == 10:
            bonus()

        elif choice == 11:
            print("Program Closed")
            break

        else:
            print("Invalid Choice")

    except ValueError:
        print("Please Enter Numbers Only")