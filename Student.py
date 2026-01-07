# Simple Student Registration System
# File: student.py

students = []
print("Welcome to Student Registration System")
while True:
    print("\n--- Student Registration Menu ---")
    print("1. Register Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student Email")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll_no = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        email = input("Enter Email ID: ")
        course = input("Enter Course Name: ")

        student = {
            "roll": roll_no,
            "name": name,
            "email": email,
            "course": course
        }

        students.append(student)
        print("Student registered successfully.")

    elif choice == "2":
        if not students:
            print("No students registered.")
        else:
            print("\nRegistered Students")
            print("-" * 40)
            for s in students:
                print("Roll No :", s["roll"])
                print("Name    :", s["name"])
                print("Email   :", s["email"])
                print("Course  :", s["course"])
                print("-" * 40)

    elif choice == "3":
        search_roll = input("Enter Roll Number to search: ")
        found = False

        for s in students:
            if s["roll"] == search_roll:
                print("\nStudent Found")
                print("Roll No :", s["roll"])
                print("Name    :", s["name"])
                print("Email   :", s["email"])
                print("Course  :", s["course"])
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "4":
        roll_no = input("Enter Roll Number to update email: ")
        updated = False

        for s in students:
            if s["roll"] == roll_no:
                new_email = input("Enter new email: ")
                s["email"] = new_email
                print("Email updated successfully.")
                updated = True
                break

        if not updated:
            print("Student not found.")

    elif choice == "5":
        roll_no = input("Enter Roll Number to delete: ")
        deleted = False

        for s in students:
            if s["roll"] == roll_no:
                students.remove(s)
                print("Student deleted successfully.")
                deleted = True
                break

        if not deleted:
            print("Student not found.")

    elif choice == "6":
        print("Exiting Student Registration System.")
        break

    else:
        print("Invalid choice. Please try again.")
