students = []
marks = []


def add_student():
    name = input("Enter student name: ")
    mark = int(input("Enter marks: "))

    students.append(name)
    marks.append(mark)

    print("Student Added Successfully")


def display_students():
    if len(students) == 0:
        print("No student records found")
    else:
        print("\n----- STUDENT RECORDS -----")

        for i in range(len(students)):
            print("Name:", students[i], "| Marks:", marks[i])


def highest_marks():
    if len(marks) == 0:
        print("No records found")
    else:
        high = marks[0]
        index = 0

        for i in range(len(marks)):
            if marks[i] > high:
                high = marks[i]
                index = i

        print("Top Student:", students[index])
        print("Highest Marks:", high)


def search_student():
    name = input("Enter student name to search: ")

    found = False

    for i in range(len(students)):
        if students[i] == name:
            print("Student Found")
            print("Marks:", marks[i])
            found = True
            break

    if found == False:
        print("Student Not Found")


def remove_student():
    name = input("Enter student name to remove: ")

    found = False

    for i in range(len(students)):
        if students[i] == name:
            students.pop(i)
            marks.pop(i)

            print("Student Removed")
            found = True
            break

    if found == False:
        print("Student Not Found")


while True:
    print("\n====== STUDENT MANAGEMENT SYSTEM ======")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Highest Marks")
    print("4. Search Student")
    print("5. Remove Student")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        display_students()
    elif choice == 3:
        highest_marks()
    elif choice == 4:
        search_student()
    elif choice == 5:
        remove_student()
    elif choice == 6:
        print("Program Closed")
        break
    else:
        print("Invalid Choice")