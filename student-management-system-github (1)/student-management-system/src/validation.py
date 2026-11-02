"""Input validation helpers."""
import re


def validate_student_id(student_id: str) -> str:
    value = student_id.strip()
    if not value:
        raise ValueError("Student ID cannot be empty.")
    if len(value) > 20:
        raise ValueError("Student ID must be 20 characters or fewer.")
    return value


def validate_name(name: str) -> str:
    value = " ".join(name.split())
    if len(value) < 2:
        raise ValueError("Name must contain at least 2 characters.")
    return value


def validate_email(email: str) -> str:
    value = email.strip()
    if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", value):
        raise ValueError("Enter a valid email address.")
    return value


def validate_subject(subject: str) -> str:
    value = " ".join(subject.split())
    if not value:
        raise ValueError("Subject cannot be empty.")
    return value


def validate_marks(marks) -> float:
    try:
        value = float(marks)
    except (TypeError, ValueError):
        raise ValueError("Marks must be a number.")
    if not 0 <= value <= 100:
        raise ValueError("Marks must be between 0 and 100.")
    return round(value, 2)
