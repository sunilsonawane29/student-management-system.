import tempfile
import unittest
from pathlib import Path
from src.service import StudentService
from src.storage import StudentStorage


class StudentServiceTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.service = StudentService(
            StudentStorage(Path(self.temp_dir.name) / "students.json")
        )

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_add_search_and_persist(self):
        self.service.add_student("S01", "Asha Patel", "asha@example.com")
        self.assertEqual(len(self.service.search_students("asha")), 1)
        reloaded = StudentService(self.service.storage)
        self.assertEqual(reloaded.get_student("S01").name, "Asha Patel")

    def test_duplicate_id_is_rejected(self):
        self.service.add_student("S01", "Asha Patel", "asha@example.com")
        with self.assertRaises(ValueError):
            self.service.add_student("S01", "Ravi Shah", "ravi@example.com")

    def test_marks_validation(self):
        self.service.add_student("S01", "Asha Patel", "asha@example.com")
        with self.assertRaises(ValueError):
            self.service.add_marks("S01", "Math", 120)


if __name__ == "__main__":
    unittest.main()
