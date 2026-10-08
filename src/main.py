import sys
from pathlib import Path

# Add project root to Python path
ROOT_DIR = Path(__file__).resolve().parent.parent

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from src.services.student_service import StudentService
from src.utils.logger import setup_logger


class StudentInformationSystem:
    """Main console interface for the Student Information System."""

    def __init__(self):
        self.logger = setup_logger()
        self.student_service = StudentService()

    def display_menu(self):
        """Display the main application menu."""

        print("\n" + "=" * 55)
        print("              STUDENT INFORMATION SYSTEM")
        print("=" * 55)
        print("[1] Add Student")
        print("[2] View All Students")
        print("[3] View Student by ID")
        print("[4] Update Student")
        print("[5] Delete Student")
        print("[6] Search Students")
        print("[7] Exit")
        print("=" * 55)

    def add_student(self):
        """Collect student information and add a student."""

        print("\n--- Add New Student ---")

        name = input("Name: ").strip()
        email = input("Email: ").strip()
        course = input("Course: ").strip()
        year_level = input("Year Level: ").strip()
        gpa_input = input("GPA (optional): ").strip()

        try:
            gpa = float(gpa_input) if gpa_input else 0.0

            student_data = {
                "name": name,
                "email": email,
                "course": course,
                "year_level": year_level,
                "gpa": gpa
            }

            student = self.student_service.add_student(student_data)

            print(
                f"\nStudent added successfully!"
                f"\nStudent ID: {student['student_id']}"
            )

        except ValueError as error:
            print(f"\nValidation error: {error}")

        except Exception as error:
            self.logger.error("Error adding student: %s", error)
            print("\nAn error occurred while adding the student.")

    def view_all_students(self):
        """Display all registered students."""

        print("\n--- All Students ---")

        try:
            students = self.student_service.get_all_students()

            if not students:
                print("No students found.")
                return

            for student in students:
                print("-" * 55)
                print(f"ID:         {student['student_id']}")
                print(f"Name:       {student['name']}")
                print(f"Email:      {student['email']}")
                print(f"Course:     {student['course']}")
                print(f"Year Level: {student['year_level']}")
                print(f"GPA:        {student.get('gpa', 0.0)}")

        except Exception as error:
            self.logger.error(
                "Error viewing students: %s",
                error
            )
            print("An error occurred while retrieving students.")

    def view_student(self):
        """Display a student using their ID."""

        print("\n--- Find Student ---")

        student_id = input("Enter Student ID: ").strip()

        try:
            student = self.student_service.get_student(student_id)

            if not student:
                print("Student not found.")
                return

            print("\nStudent Details")
            print("-" * 40)

            for key, value in student.items():
                print(f"{key}: {value}")

        except Exception as error:
            self.logger.error(
                "Error finding student %s: %s",
                student_id,
                error
            )
            print("An error occurred while finding the student.")

    def search_students(self):
        """Search students using a keyword."""

        print("\n--- Search Students ---")

        keyword = input(
            "Enter name, email, course, year level, or ID: "
        ).strip()

        if not keyword:
            print("Search keyword cannot be empty.")
            return

        try:
            students = self.student_service.search_students(keyword)

            if not students:
                print("\nNo matching students found.")
                return

            print(f"\nFound {len(students)} student(s):")
            print("-" * 55)

            for student in students:
                print(f"ID:         {student['student_id']}")
                print(f"Name:       {student['name']}")
                print(f"Email:      {student['email']}")
                print(f"Course:     {student['course']}")
                print(f"Year Level: {student['year_level']}")
                print(f"GPA:        {student.get('gpa', 0.0)}")
                print("-" * 55)

        except Exception as error:
            self.logger.error(
                "Error searching students: %s",
                error
            )
            print("An error occurred while searching.")

    def update_student(self):
        """Update an existing student's information."""

        print("\n--- Update Student ---")

        student_id = input("Enter Student ID: ").strip()

        try:
            student = self.student_service.get_student(student_id)

            if not student:
                print("Student not found.")
                return

            print("Press Enter to keep the current value.")

            name = input(
                f"Name [{student['name']}]: "
            ).strip()

            email = input(
                f"Email [{student['email']}]: "
            ).strip()

            course = input(
                f"Course [{student['course']}]: "
            ).strip()

            year_level = input(
                f"Year Level [{student['year_level']}]: "
            ).strip()

            gpa_input = input(
                f"GPA [{student.get('gpa', 0.0)}]: "
            ).strip()

            update_data = {}

            if name:
                update_data["name"] = name

            if email:
                update_data["email"] = email

            if course:
                update_data["course"] = course

            if year_level:
                update_data["year_level"] = year_level

            if gpa_input:
                update_data["gpa"] = float(gpa_input)

            updated = self.student_service.update_student(
                student_id,
                update_data
            )

            if updated:
                print("Student updated successfully.")
            else:
                print("Student not found.")

        except ValueError:
            print("Invalid GPA. Update cancelled.")

        except Exception as error:
            self.logger.error(
                "Error updating student %s: %s",
                student_id,
                error
            )
            print("An error occurred while updating the student.")

    def delete_student(self):
        """Delete a student after confirmation."""

        print("\n--- Delete Student ---")

        student_id = input("Enter Student ID: ").strip()

        try:
            student = self.student_service.get_student(student_id)

            if not student:
                print("Student not found.")
                return

            confirm = input(
                f"Delete {student['name']} ({student_id})? [y/N]: "
            ).strip().lower()

            if confirm == "y":

                if self.student_service.delete_student(student_id):
                    print("Student deleted successfully.")
                else:
                    print("Student not found.")

            else:
                print("Delete cancelled.")

        except Exception as error:
            self.logger.error(
                "Error deleting student %s: %s",
                student_id,
                error
            )
            print("An error occurred while deleting the student.")

    def run(self):
        """Run the main application loop."""

        self.logger.info("Student Information System started.")

        while True:

            self.display_menu()

            choice = input(
                "Enter your choice (1-7): "
            ).strip()

            if choice == "1":
                self.add_student()

            elif choice == "2":
                self.view_all_students()

            elif choice == "3":
                self.view_student()

            elif choice == "4":
                self.update_student()

            elif choice == "5":
                self.delete_student()

            elif choice == "6":
                self.search_students()

            elif choice == "7":
                self.logger.info(
                    "Student Information System closed."
                )

                print("\nThank you for using the Student Information System!")
                break

            else:
                print(
                    "\nInvalid choice. Please select an option from 1 to 6."
                )


if __name__ == "__main__":
    app = StudentInformationSystem()
    app.run()