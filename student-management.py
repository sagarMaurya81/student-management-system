# ============================================================
# Student Management CLI Application
# ============================================================

students = []


# ------------------------------------------------------------
# Utility Functions
# ------------------------------------------------------------

def get_valid_student_id():
    """Get a valid numeric student ID."""
    while True:
        try:
            student_id = int(input("Enter Student ID: "))

            if student_id <= 0:
                print(" Student ID must be greater than 0.")
                continue

            return student_id

        except ValueError:
            print(" Invalid input. Student ID must be a number.")


def get_valid_name():
    """Get a valid student name."""
    while True:
        name = input("Enter Student Name: ").strip()

        if not name:
            print(" Name cannot be empty.")
            continue

        if len(name) < 2:
            print(" Name must contain at least 2 characters.")
            continue

        if not all(char.isalpha() or char.isspace() for char in name):
            print(" Name can contain only letters and spaces.")
            continue

        return name


def get_valid_age():
    """Get a valid student age."""
    while True:
        try:
            age = int(input("Enter Age: "))

            if age < 1 or age > 100:
                print(" Age must be between 1 and 100.")
                continue

            return age

        except ValueError:
            print(" Invalid input. Age must be a number.")


def get_valid_city():
    """Get a valid city."""
    while True:
        city = input("Enter City: ").strip()

        if not city:
            print(" City cannot be empty.")
            continue

        if not all(char.isalpha() or char.isspace() for char in city):
            print(" City can contain only letters and spaces.")
            continue

        return city


def find_student(student_id):
    """Find a student using Student ID."""
    for student in students:
        if student["id"] == student_id:
            return student

    return None


# ------------------------------------------------------------
# Add Student
# ------------------------------------------------------------

def add_student():
    print("\n========== ADD STUDENT ==========")

    student_id = get_valid_student_id()

    # Check duplicate ID
    if find_student(student_id):
        print(" Student ID already exists.")
        return

    name = get_valid_name()
    age = get_valid_age()
    city = get_valid_city()

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "city": city
    }

    students.append(student)

    print(" Student added successfully!")


# ------------------------------------------------------------
# View Students
# ------------------------------------------------------------

def view_students():
    print("\n========== ALL STUDENTS ==========")

    if not students:
        print(" No students found.")
        return

    print("-" * 65)
    print(f"{'ID':<10}{'Name':<25}{'Age':<10}{'City':<20}")
    print("-" * 65)

    for student in students:
        print(
            f"{student['id']:<10}"
            f"{student['name']:<25}"
            f"{student['age']:<10}"
            f"{student['city']:<20}"
        )

    print("-" * 65)


# ------------------------------------------------------------
# Search Student
# ------------------------------------------------------------

def search_student():
    print("\n========== SEARCH STUDENT ==========")

    if not students:
        print(" No students available.")
        return

    keyword = input("Enter student ID or name: ").strip()

    if not keyword:
        print(" Search value cannot be empty.")
        return

    found_students = []

    for student in students:

        # Search by ID
        if keyword.isdigit() and student["id"] == int(keyword):
            found_students.append(student)

        # Search by name
        elif keyword.lower() in student["name"].lower():
            found_students.append(student)

    if not found_students:
        print(" No student found.")
        return

    print("\nStudents Found:")
    print("-" * 65)

    for student in found_students:
        print(f"ID    : {student['id']}")
        print(f"Name  : {student['name']}")
        print(f"Age   : {student['age']}")
        print(f"City  : {student['city']}")
        print("-" * 65)


# ------------------------------------------------------------
# Display Student Details
# ------------------------------------------------------------

def display_student_details():
    print("\n========== STUDENT DETAILS ==========")

    if not students:
        print(" No students available.")
        return

    student_id = get_valid_student_id()

    student = find_student(student_id)

    if student is None:
        print(" Student not found.")
        return

    print("\nStudent Information")
    print("-" * 40)
    print(f"Student ID : {student['id']}")
    print(f"Name       : {student['name']}")
    print(f"Age        : {student['age']}")
    print(f"City       : {student['city']}")
    print("-" * 40)


# ------------------------------------------------------------
# Update Student
# ------------------------------------------------------------

def update_student():
    print("\n========== UPDATE STUDENT ==========")

    if not students:
        print(" No students available.")
        return

    student_id = get_valid_student_id()

    student = find_student(student_id)

    if student is None:
        print(" Student not found.")
        return

    print("\nCurrent Student Details:")
    print(f"Name : {student['name']}")
    print(f"Age  : {student['age']}")
    print(f"City : {student['city']}")

    print("\nEnter new details:")

    student["name"] = get_valid_name()
    student["age"] = get_valid_age()
    student["city"] = get_valid_city()

    print(" Student updated successfully!")


# ------------------------------------------------------------
# Delete Student
# ------------------------------------------------------------

def delete_student():
    print("\n========== DELETE STUDENT ==========")

    if not students:
        print(" No students available.")
        return

    student_id = get_valid_student_id()

    student = find_student(student_id)

    if student is None:
        print(" Student not found.")
        return

    print("\nStudent to delete:")
    print(f"ID   : {student['id']}")
    print(f"Name : {student['name']}")

    confirmation = input("Are you sure? (y/n): ").strip().lower()

    if confirmation not in ("y", "yes"):
        print(" Delete operation cancelled.")
        return

    students.remove(student)

    print(" Student deleted successfully!")


# ------------------------------------------------------------
# Main Menu
# ------------------------------------------------------------

def display_menu():
    print("\n")
    print("=" * 50)
    print("       STUDENT MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Display Student Details")
    print("7. Exit")
    print("=" * 50)


def main():
    print("\nWelcome to Student Management System!")

    while True:
        try:
            display_menu()

            choice = input("Enter your choice (1-7): ").strip()

            if choice == "1":
                add_student()

            elif choice == "2":
                view_students()

            elif choice == "3":
                search_student()

            elif choice == "4":
                update_student()

            elif choice == "5":
                delete_student()

            elif choice == "6":
                display_student_details()

            elif choice == "7":
                print("\nThank you for using Student Management System!")
                print("Goodbye ")
                break

            else:
                print(" Invalid choice. Please select 1-7.")

        except KeyboardInterrupt:
            print("\n\n Program interrupted by user.")
            print("Exiting safely...")
            break

        except Exception as e:
            print(f" Unexpected error: {e}")


# ------------------------------------------------------------
# Program Entry Point
# ------------------------------------------------------------

if __name__ == "__main__":
    main()