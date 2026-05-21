inventory = 100

def get_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        return None

def main():
    global inventory
    while True:
        print("\n===== PRODUCTION MANAGEMENT =====")
        print("1. Check Inventory")
        print("2. Produce Items")
        print("3. Consume Items")
        print("4. Exit")
        choice = get_int("Enter your choice: ")
        if choice is None:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            print("Current Inventory =", inventory)
        elif choice == 2:
            qty = get_int("Enter quantity to produce: ")
            if qty is None:
                print("Invalid quantity. Please enter a whole number.")
                continue
            if qty > 0:
                inventory += qty
                print("Production recorded successfully.")
                print("Updated Inventory =", inventory)
            else:
                print("Quantity must be positive.")
        elif choice == 3:
            qty = get_int("Enter quantity to consume: ")
            if qty is None:
                print("Invalid quantity. Please enter a whole number.")
                continue
            if qty <= inventory and qty > 0:
                inventory -= qty
                print("Consumption recorded successfully.")
                print("Remaining Inventory =", inventory)
            elif qty <= 0:
                print("Quantity must be positive.")
            else:
                print("Insufficient Inventory")
        elif choice == 4:
            print("Thank you for using Production Management")
            break
        else:
            print("Invalid Choice! Please Try Again")

if __name__ == '__main__':
    main()
