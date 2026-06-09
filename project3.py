library = []
def add_book():
    book = {}
    book["id"] = int(input("Enter Book ID: "))
    book["name"] = input("Enter Book Name: ")
    book["author"] = input("Enter Author Name: ")
    book["issued"] = False

    library.append(book)

    print("Book Added Successfully")


def display_books():

    if len(library) == 0:
        print("No Books Available")

    else:
        print("\n------ BOOK RECORDS ------")

        for book in library:

            print("ID:", book["id"])
            print("Name:", book["name"])
            print("Author:", book["author"])

            if book["issued"] == True:
                print("Status: Issued")
            else:
                print("Status: Available")

            print("--------------------------")


def search_book():

    search = input("Enter Book Name: ")

    found = False

    for book in library:

        if book["name"].lower() == search.lower():

            print("\nBook Found")
            print("ID:", book["id"])
            print("Author:", book["author"])

            if book["issued"] == True:
                print("Status: Issued")
            else:
                print("Status: Available")

            found = True
            break

    if found == False:
        print("Book Not Found")


def issue_book():

    book_id = int(input("Enter Book ID to Issue: "))

    found = False

    for book in library:

        if book["id"] == book_id:

            if book["issued"] == False:
                book["issued"] = True
                print("Book Issued Successfully")

            else:
                print("Book Already Issued")

            found = True
            break

    if found == False:
        print("Book ID Not Found")


def return_book():

    book_id = int(input("Enter Book ID to Return: "))

    found = False

    for book in library:

        if book["id"] == book_id:

            if book["issued"] == True:
                book["issued"] = False
                print("Book Returned Successfully")

            else:
                print("Book was not issued")

            found = True
            break

    if found == False:
        print("Book ID Not Found")


def remove_book():

    book_id = int(input("Enter Book ID to Remove: "))

    found = False

    for book in library:

        if book["id"] == book_id:
            library.remove(book)

            print("Book Removed Successfully")

            found = True
            break

    if found == False:
        print("Book ID Not Found")


while True:

    print("\n====== LIBRARY MANAGEMENT SYSTEM ======")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Remove Book")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_book()

    elif choice == 2:
        display_books()

    elif choice == 3:
        search_book()

    elif choice == 4:
        issue_book()

    elif choice == 5:
        return_book()

    elif choice == 6:
        remove_book()

    elif choice == 7:
        print("Program Closed")
        break

    else:
        print("Invalid Choice")