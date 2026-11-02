"""Student data model and grade calculations."""
from dataclasses import dataclass, field, asdict
from typing import Dict


@dataclass
class Student:
    student_id: str
    name: str
    email: str
    marks: Dict[str, float] = field(default_factory=dict)

    def total_marks(self) -> float:
        return round(sum(self.marks.values()), 2)

    def percentage(self) -> float:
        if not self.marks:
            return 0.0
        return round(self.total_marks() / len(self.marks), 2)

    def grade(self) -> str:
        score = self.percentage()
        if not self.marks:
            return "N/A"
        if score >= 80:
            return "A"
        if score >= 70:
            return "B"
        if score >= 60:
            return "C"
        if score >= 50:
            return "D"
        return "F"

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Student":
        return cls(
            student_id=str(data["student_id"]),
            name=str(data["name"]),
            email=str(data["email"]),
            marks={str(k): float(v) for k, v in data.get("marks", {}).items()},
        )
