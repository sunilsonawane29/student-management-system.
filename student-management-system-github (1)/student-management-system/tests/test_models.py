import unittest
from src.models import Student


class StudentModelTests(unittest.TestCase):
    def test_grade_and_percentage(self):
        student = Student("S1", "Asha", "asha@example.com", {"Math": 90, "English": 70})
        self.assertEqual(student.percentage(), 80)
        self.assertEqual(student.grade(), "A")

    def test_empty_marks(self):
        student = Student("S2", "Ravi", "ravi@example.com")
        self.assertEqual(student.percentage(), 0)
        self.assertEqual(student.grade(), "N/A")


if __name__ == "__main__":
    unittest.main()
