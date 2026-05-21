balance = 1000
while True:
    print("\n===== BANK APPLICATION =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Current Balance =", balance)
    elif choice == 2:
        deposit = int(input("Enter amount to deposit: "))

        if deposit > 0:
            balance = balance + deposit
            print("Amount Deposited Successfully")
            print("Updated Balance =", balance)
        else:
            print("Invalid Deposit Amount")
    elif choice == 3:
        withdraw = int(input("Enter amount to withdraw: "))

        if withdraw <= balance:
            balance = balance - withdraw
            print("Withdrawal Successful")
            print("Remaining Balance =", balance)
        else:
            print("Insufficient Balance")
    elif choice == 4:
        print("Thank You for Using Bank Application")
        break
    else:
        print("Invalid Choice! Please Try Again")