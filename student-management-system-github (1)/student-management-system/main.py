"""Application entry point."""
from src.cli import run_app
from src.service import StudentService
from src.storage import StudentStorage


def main():
    service = StudentService(StudentStorage())
    run_app(service)


if __name__ == "__main__":
    main()
