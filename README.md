# Student Information System

Python console-based Student Information System based on the sample implementation.

## Features
- Create/Add student
- Read/View all students
- Read/View student by ID
- Update student
- Delete student
- JSON file storage
- Application logging

## Project Structure
```text
student_information_system/
├── data/
│   └── students.json
├── logs/
├── src/
│   ├── models/
│   │   └── student.py
│   └── services/
│       └── student_service.py
├── main.py
└── README.md
```

## Run
From the project folder:

```bash
python main.py
```

The application automatically creates `data/students.json` and `logs/app.log` when needed.

## Note
The screenshots show update/delete as placeholders (`pass`). This version completes those CRUD operations so the project is fully functional.
