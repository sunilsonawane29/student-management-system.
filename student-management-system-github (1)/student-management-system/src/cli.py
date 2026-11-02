"""Interactive command-line interface."""
from src.reports import student_summary


def _prompt_required(label):
    value = input(label).strip()
    if not value:
        raise ValueError("This field is required.")
    return value


def run_app(service):
    print("\n=== Student Management System ===")
    while True:
        print(
            "\n1. Add student\n2. List students\n3. Search students\n"
            "4. Update student\n5. Delete student\n6. Add/update marks\n"
            "7. View student report\n0. Exit"
        )
        choice = input("Choose an option: ").strip()
        try:
            if choice == "1":
                student = service.add_student(
                    _prompt_required("Student ID: "),
                    _prompt_required("Name: "),
                    _prompt_required("Email: "),
                )
                print(f"Added {student.name}.")
            elif choice == "2":
                students = service.list_students()
                if not students:
                    print("No student records found.")
                for student in students:
                    print(f"{student.student_id} | {student.name} | {student.email}")
            elif choice == "3":
                for student in service.search_students(input("Search: ")):
                    print(f"{student.student_id} | {student.name} | {student.email}")
            elif choice == "4":
                sid = _prompt_required("Student ID: ")
                name = input("New name (leave blank to keep current): ").strip() or None
                email = input("New email (leave blank to keep current): ").strip() or None
                service.update_student(sid, name, email)
                print("Student updated.")
            elif choice == "5":
                service.delete_student(_prompt_required("Student ID: "))
                print("Student deleted.")
            elif choice == "6":
                service.add_marks(
                    _prompt_required("Student ID: "),
                    _prompt_required("Subject: "),
                    _prompt_required("Marks (0-100): "),
                )
                print("Marks saved.")
            elif choice == "7":
                student = service.get_student(_prompt_required("Student ID: "))
                print("\n" + student_summary(student))
            elif choice == "0":
                print("Goodbye!")
                break
            else:
                print("Please choose a valid menu option.")
        except (ValueError, RuntimeError) as exc:
            print(f"Error: {exc}")
