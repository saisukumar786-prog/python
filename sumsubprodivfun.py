def sum(a, b):
    return a + b


def difference(a, b):
    return a - b


def product(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b


while True:
    print("------------simple calculator------------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '5':
        print("Exiting the calculator. Goodbye!")
        break

    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice. Please enter a number between 1 and 5.")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("The sum of num1 and num2 is:", sum(num1, num2))
    elif choice == '2':
        print("The difference of num1 and num2 is:", difference(num1, num2))
    elif choice == '3':
        print("The product of num1 and num2 is:", product(num1, num2))
    elif choice == '4':
        print("The division of num1 by num2 is:", divide(num1, num2))
