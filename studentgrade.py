while True:
    print("\n-------- MENU ------------")
    print("1. Check Grade")
    print("2. Multiplication Table")
    print("3. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        marks = int(input("Enter student marks: "))

        if marks >= 90:
            print("Grade: A+")
        elif marks >= 75:
            print("Grade: A")
        elif marks >= 60:
            print("Grade: B")
        elif marks >= 40:
            print("Grade: C")
        else:
            print("Grade: Fail")

    elif choice == 2:
        num = int(input("Enter a number: "))
        print("\nMultiplication Table:")
        for i in range(1, 11):
            print(num, "x", i, "=", num * i)
    elif choice == 3:
        print("Exiting Application...")
        break
    else:
        print("Invalid Choice! Please try again.")