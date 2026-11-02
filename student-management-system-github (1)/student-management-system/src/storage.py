"""JSON persistence for student records."""
import json
from pathlib import Path
from typing import Dict
from src.models import Student


class StudentStorage:
    def __init__(self, file_path="data/students.json"):
        self.file_path = Path(file_path)

    def load(self) -> Dict[str, Student]:
        if not self.file_path.exists():
            return {}
        try:
            raw = json.loads(self.file_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as exc:
            raise RuntimeError(f"Could not read student database: {exc}") from exc
        return {sid: Student.from_dict(item) for sid, item in raw.items()}

    def save(self, students: Dict[str, Student]) -> None:
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        payload = {sid: student.to_dict() for sid, student in students.items()}
        temporary = self.file_path.with_suffix(self.file_path.suffix + ".tmp")
        temporary.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        temporary.replace(self.file_path)
