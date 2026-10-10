
import sys
import tempfile
import unittest
from pathlib import Path

# Add the project root for the embeddable Python environment.
ROOT_DIR = Path(__file__).resolve().parent.parent

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from src.services.student_service import StudentService


class TestStudentService(unittest.TestCase):
    """Test student CRUD, search, validation, and CSV export."""

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.data_file = Path(self.temp_dir.name) / "students.json"
        self.service = StudentService(data_file=self.data_file)

        self.student_data = {
            "student_id": "TEST-001",
            "name": "Juan Dela Cruz",
            "email": "juan@example.com",
            "course": "BSIT",
            "year_level": "2",
            "gpa": 1.75,
        }

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_add_and_retrieve_student(self):
        added = self.service.add_student(self.student_data)

        self.assertEqual(added["student_id"], "TEST-001")
        self.assertEqual(
            self.service.get_student("TEST-001")["name"],
            "Juan Dela Cruz",
        )

    def test_get_all_students(self):
        self.service.add_student(self.student_data)

        students = self.service.get_all_students()

        self.assertEqual(len(students), 1)

    def test_search_students(self):
        self.service.add_student(self.student_data)

        results = self.service.search_students("juan")

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["student_id"], "TEST-001")

    def test_update_student(self):
        self.service.add_student(self.student_data)

        updated = self.service.update_student(
            "TEST-001",
            {"name": "Juan Updated"},
        )

        self.assertIsNotNone(updated)
        self.assertEqual(updated["name"], "Juan Updated")

    def test_delete_student(self):
        self.service.add_student(self.student_data)

        deleted = self.service.delete_student("TEST-001")

        self.assertTrue(deleted)
        self.assertIsNone(self.service.get_student("TEST-001"))

    def test_invalid_student_is_rejected(self):
        invalid_data = self.student_data.copy()
        invalid_data["name"] = ""

        with self.assertRaises(ValueError):
            self.service.add_student(invalid_data)

        self.assertEqual(self.service.get_all_students(), [])

    def test_export_to_csv(self):
        self.service.add_student(self.student_data)

        export_file = Path(self.temp_dir.name) / "students_export.csv"
        result = self.service.export_to_csv(str(export_file))

        self.assertTrue(result)
        self.assertTrue(export_file.exists())

        content = export_file.read_text(encoding="utf-8")
        self.assertIn("Juan Dela Cruz", content)
        self.assertIn("juan@example.com", content)


if __name__ == "__main__":
    unittest.main(verbosity=2)
