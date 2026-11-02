"""Formatting helpers for student results."""
def student_summary(student):
    marks_text = ", ".join(
        f"{subject}: {score:g}" for subject, score in sorted(student.marks.items())
    ) or "No marks entered"
    return (
        f"ID: {student.student_id}\n"
        f"Name: {student.name}\n"
        f"Email: {student.email}\n"
        f"Marks: {marks_text}\n"
        f"Total: {student.total_marks():g}\n"
        f"Percentage: {student.percentage():g}%\n"
        f"Grade: {student.grade()}"
    )
