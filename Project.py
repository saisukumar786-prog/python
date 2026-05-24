import math
import random

def factorial_num(n):
    return math.factorial(n)

def prime_check(n):
    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True
 
def square_root(n):
    return math.sqrt(n)

def power_num(a, b):
    return math.pow(a, b)

def gcd_num(a, b):
    return math.gcd(a, b)

def trig_values(angle):
    rad = math.radians(angle)

    print("Sin =", math.sin(rad))
    print("Cos =", math.cos(rad))
    print("Tan =", math.tan(rad))

while True:
    print("\n====== NUMBER UTILITY PROJECT ======")
    print("1. Factorial")
    print("2. Prime Check")
    print("3. Square Root")
    print("4. Power")
    print("5. GCD")
    print("6. Random Number")
    print("7. Trigonometry")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        num = int(input("Enter number: "))
        print("Factorial =", factorial_num(num))

    elif choice == 2:
        num = int(input("Enter number: "))

        if prime_check(num):
            print(num, "is Prime")
        else:
            print(num, "is Not Prime")

    elif choice == 3:
        num = int(input("Enter number: "))
        print("Square Root =", square_root(num))

    elif choice == 4:
        a = int(input("Enter base number: "))
        b = int(input("Enter power: "))
        print("Result =", power_num(a, b))

    elif choice == 5:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("GCD =", gcd_num(a, b))

    elif choice == 6:
        print("Random Number =", random.randint(1, 100))

    elif choice == 7:
        angle = float(input("Enter angle in degrees: "))
        trig_values(angle)

    elif choice == 8:
        print("Program Closed")
        break

    else:
        print("Invalid Choice")