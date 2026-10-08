import json
from datetime import datetime

from src.models.student import Student
from src.utils.config import get_data_file
from src.utils.logger import setup_logger
from src.utils.validators import validate_student_data


class StudentService:
    """Handles student data management and JSON persistence."""

    def __init__(self, data_file=None):
        self.data_file = data_file or get_data_file()
        self.logger = setup_logger()

        self._ensure_data_file()

    def _ensure_data_file(self):
        """Create the data directory and JSON file if they do not exist."""

        try:
            self.data_file.parent.mkdir(parents=True, exist_ok=True)

            if not self.data_file.exists():
                with open(self.data_file, "w", encoding="utf-8") as file:
                    json.dump([], file, indent=2)

                self.logger.info(
                    "Created student data file: %s",
                    self.data_file
                )

        except OSError as error:
            self.logger.error(
                "Unable to create data file: %s",
                error
            )
            raise

    def _load_students(self):
        """Load students from the JSON data file."""

        try:
            with open(self.data_file, "r", encoding="utf-8") as file:
                data = json.load(file)

            if not isinstance(data, list):
                raise ValueError("Student data must be a JSON list.")

            return data

        except FileNotFoundError:
            self.logger.warning(
                "Student data file was missing. Recreating it."
            )

            self._ensure_data_file()
            return []

        except json.JSONDecodeError as error:
            self.logger.error(
                "Invalid JSON data: %s",
                error
            )

            raise ValueError(
                "Student data file contains invalid JSON."
            )

        except OSError as error:
            self.logger.error(
                "Unable to read student data: %s",
                error
            )
            raise

    def _save_students(self, students):
        """Save students to the JSON data file."""

        try:
            with open(self.data_file, "w", encoding="utf-8") as file:
                json.dump(students, file, indent=2)

        except OSError as error:
            self.logger.error(
                "Unable to save student data: %s",
                error
            )
            raise

    def add_student(self, student_data):
        """Add a new student."""

        is_valid, message = validate_student_data(student_data)

        if not is_valid:
            self.logger.warning(
                "Student validation failed: %s",
                message
            )
            raise ValueError(message)

        students = self._load_students()

        student = Student(
            student_id=student_data.get("student_id"),
            name=student_data["name"],
            email=student_data["email"],
            course=student_data["course"],
            year_level=student_data["year_level"],
            gpa=student_data.get("gpa", 0.0)
        )

        students.append(student.to_dict())
        self._save_students(students)

        self.logger.info(
            "Student added successfully: %s",
            student.student_id
        )

        return student.to_dict()

    def get_all_students(self):
        """Return all students."""

        return self._load_students()

    def get_student(self, student_id):
        """Find a student by ID."""

        students = self._load_students()

        for student in students:
            if student["student_id"] == student_id:
                return student

        return None
    
    def search_students(self, keyword):
        """Search students by name, email, course, or student ID."""

        keyword = keyword.strip().lower()

        if not keyword:
            return []

        students = self._load_students()

        results = []

        for student in students:
            searchable_fields = [
                student.get("student_id", ""),
                student.get("name", ""),
                student.get("email", ""),
                student.get("course", ""),
                student.get("year_level", "")
            ]

            if any(
                keyword in str(field).lower()
                for field in searchable_fields
            ):
                results.append(student)

        self.logger.info(
            "Student search performed: '%s' - %d result(s)",
            keyword,
            len(results)
        )

        return results

    def update_student(self, student_id, update_data):
        """Update an existing student's information."""

        students = self._load_students()

        for student in students:
            if student["student_id"] == student_id:

                student.update(update_data)
                student["student_id"] = student_id
                student["updated_at"] = datetime.now().isoformat()

                self._save_students(students)

                self.logger.info(
                    "Student updated successfully: %s",
                    student_id
                )

                return student

        return None

    def delete_student(self, student_id):
        """Delete a student by ID."""

        students = self._load_students()

        updated_students = [
            student
            for student in students
            if student["student_id"] != student_id
        ]

        if len(updated_students) == len(students):
            return False

        self._save_students(updated_students)

        self.logger.info(
            "Student deleted successfully: %s",
            student_id
        )

        return True