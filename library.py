# Simple Library Management System

library = []

while True:
    print("\n--- Library Menu ---")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Name: ")
        copies = int(input("Enter Number of Copies: "))

        library.append([book_id, title, copies])
        print("Book added successfully")

    elif choice == "2":
        if not library:
            print("No books available")
        else:
            print("\nBook ID | Book Name | Copies")
            for book in library:
                print(book[0], " | ", book[1], " | ", book[2])

    elif choice == "3":
        book_id = input("Enter Book ID to issue: ")
        found = False

        for book in library:
            if book[0] == book_id:
                if book[2] > 0:
                    book[2] -= 1
                    print("Book issued successfully")
                else:
                    print("No copies available")
                found = True
                break

        if not found:
            print("Book not found")

    elif choice == "4":
        print("Thank you for using Library System")
        break

    else:
        print("Invalid choice, try again")

