# Student Management System

A beginner-friendly Python command-line application for managing student records and marks. Data is stored locally in a JSON file, so records remain available after the program closes.

## Features
- Add, list, search, update and delete students
- Record marks for subjects
- Calculate total, percentage and grade
- Validate student details and marks
- Save records in `data/students.json`

## Requirements
- Python 3.9 or newer
- No third-party packages required to run the application

## Run
From the project root:

```bash
python main.py
```

The application creates the `data/` folder and JSON database automatically when needed.

## Run tests
```bash
python -m unittest discover -s tests -v
```

## Project structure
```text
student-management-system/
├── data/
├── docs/
├── src/
├── tests/
├── main.py
└── README.md
```

## Grade scale
- A: 80–100%
- B: 70–79.99%
- C: 60–69.99%
- D: 50–59.99%
- F: Below 50%

This is an educational project. Keep backups of the JSON data file before making manual changes.
