"""Business logic for student records."""
from src.models import Student
from src.validation import (
    validate_email, validate_marks, validate_name,
    validate_student_id, validate_subject,
)


class StudentService:
    def __init__(self, storage):
        self.storage = storage
        self.students = storage.load()

    def _save(self):
        self.storage.save(self.students)

    def add_student(self, student_id, name, email):
        sid = validate_student_id(student_id)
        if sid in self.students:
            raise ValueError("A student with this ID already exists.")
        student = Student(sid, validate_name(name), validate_email(email))
        self.students[sid] = student
        self._save()
        return student

    def list_students(self):
        return sorted(self.students.values(), key=lambda item: item.name.lower())

    def get_student(self, student_id):
        sid = validate_student_id(student_id)
        if sid not in self.students:
            raise ValueError("Student not found.")
        return self.students[sid]

    def search_students(self, query):
        q = query.strip().lower()
        return [
            student for student in self.list_students()
            if q in student.student_id.lower()
            or q in student.name.lower()
            or q in student.email.lower()
        ]

    def update_student(self, student_id, name=None, email=None):
        student = self.get_student(student_id)
        if name is not None:
            student.name = validate_name(name)
        if email is not None:
            student.email = validate_email(email)
        self._save()
        return student

    def delete_student(self, student_id):
        student = self.get_student(student_id)
        del self.students[student.student_id]
        self._save()

    def add_marks(self, student_id, subject, marks):
        student = self.get_student(student_id)
        subject_name = validate_subject(subject)
        student.marks[subject_name] = validate_marks(marks)
        self._save()
        return student
