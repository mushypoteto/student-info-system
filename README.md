# Student Information System

A Python-based, console-driven Student Information System that manages student records using JSON file storage. The project demonstrates modular software architecture, data validation, application logging, automated testing, and Git-based collaboration workflows.

## Features

### Student Management

- Add new student records
- View all students
- Find a student by ID
- Update student information
- Delete student records
- Search by student ID, name, email, course, or year level

### Data Management

- Persistent storage using JSON
- Export student records to CSV
- Automatic creation of the data file when missing
- Input validation for names, email addresses, courses, year levels, and GPA

### Application Architecture

- Modular organization using models, services, and utility modules
- Centralized application configuration
- File and console logging
- Error handling for invalid input and file operations
- Rotating log files to limit log-file growth

### Testing

- Automated unit tests using Python's built-in `unittest` framework
- Tests for adding, retrieving, updating, deleting, searching, validation, and CSV export

## Technologies Used

- **Language:** Python
- **Data storage:** JSON
- **Export format:** CSV
- **Testing:** `unittest`
- **Version control:** Git and GitHub
- **Development environment:** Visual Studio Code

The project currently uses Python standard-library modules and does not require third-party packages.

## Project Structure

```text
student_information_system/
├── config/
│   └── config.json
├── data/
│   └── students.json
├── logs/
│   └── app.log
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── student.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── student_service.py
│   └── utils/
│       ├── __init__.py
│       ├── config.py
│       ├── logger.py
│       └── validators.py
├── tests/
│   ├── __init__.py
│   └── test_student_service.py
├── .gitignore
├── README.md
└── requirements.txt
```

### Main Components

| Component                         | Responsibility                                                       |
| --------------------------------- | -------------------------------------------------------------------- |
| `src/main.py`                     | Console menu and application interaction                             |
| `src/models/student.py`           | Student data model                                                   |
| `src/services/student_service.py` | Student CRUD operations, JSON persistence, searching, and CSV export |
| `src/utils/config.py`             | Loads application settings                                           |
| `src/utils/logger.py`             | Configures application logging                                       |
| `src/utils/validators.py`         | Validates student information                                        |
| `config/config.json`              | Application configuration                                            |
| `data/students.json`              | Persistent student records                                           |
| `tests/test_student_service.py`   | Automated unit tests                                                 |

## Requirements

- Python 3.10 or newer is recommended.
- Git
- Visual Studio Code or another Python-compatible editor

No third-party Python packages are currently required.

## Installation and Execution

### 1. Clone the repository

```bash
git clone https://github.com/mushypoteto/student-info-system.git
cd student-info-system
```

### 2. Run the application

From the project root, run:

```bash
python src/main.py
```

Follow the numbered menu to manage student records.

The application uses the configuration file to determine the data and log locations. Missing data files and required directories are created when needed.

## Running Unit Tests

From the project root, run:

```bash
python tests/test_student_service.py
```

The tests use temporary files so they do not modify the project's actual student database.

The current test suite covers:

1. Adding and retrieving a student
2. Retrieving all students
3. Searching student records
4. Updating student information
5. Deleting a student
6. Rejecting invalid student data
7. Exporting student records to CSV

## Configuration and Logging

Application settings are stored in `config/config.json`.

Example configuration:

```json
{
  "data_file": "data/students.json",
  "log_file": "logs/app.log",
  "log_level": "INFO"
}
```

The logging utility records application activity, warnings, and errors to the configured log file and console. Log rotation helps prevent the log file from growing indefinitely.

## Data Storage and Export

Student records are stored in `data/students.json`. The application loads the records when needed and saves changes to the JSON file.

CSV exports are generated at:

```text
data/students_export.csv
```

The exported file can be opened using spreadsheet software such as Microsoft Excel. Generated CSV exports are excluded from Git tracking.

## Git and GitHub Workflow

The repository uses Git for version control and GitHub for remote hosting.

The development workflow includes:

- A `main` branch for integrated project changes
- Feature branches for separate development tasks
- Descriptive commit messages
- Pushing branches to GitHub
- Merging completed work into `main`

Example commands:

```bash
git checkout -b feature/example
git add .
git commit -m "feat: describe the change"
git push -u origin feature/example
```

## Known Limitations

- The application uses local JSON storage rather than a cloud-hosted database.
- The interface is console-based rather than graphical.
- The application does not currently include user authentication or role-based access control.
- CSV export requires student records to be available.

## Project Objective

This project demonstrates student-record management, modular Python development, persistent data storage, configuration management, validation, logging, testing, and GitHub-based version control in a maintainable application structure.

## License

No license has been specified for this project yet.
