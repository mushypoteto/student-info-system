import re


def validate_name(name):
    """Validate a student's name."""

    name = name.strip()

    if not name:
        return False, "Name cannot be empty."

    if len(name) < 2:
        return False, "Name must contain at least 2 characters."

    if len(name) > 100:
        return False, "Name must not exceed 100 characters."

    if not re.match(r"^[A-Za-zÀ-ÿ .'-]+$", name):
        return False, "Name contains invalid characters."

    return True, ""


def validate_email(email):
    """Validate an email address."""

    email = email.strip()

    if not email:
        return False, "Email cannot be empty."

    pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

    if not re.match(pattern, email):
        return False, "Please enter a valid email address."

    return True, ""


def validate_course(course):
    """Validate the student's course."""

    course = course.strip()

    if not course:
        return False, "Course cannot be empty."

    if len(course) < 2:
        return False, "Course must contain at least 2 characters."

    return True, ""


def validate_year_level(year_level):
    """Validate the student's year level."""

    year_level = year_level.strip()

    valid_year_levels = {
        "1", "2", "3", "4",
        "1st", "2nd", "3rd", "4th"
    }

    if year_level.lower() not in valid_year_levels:
        return False, "Invalid year level."

    return True, ""


def validate_gpa(gpa):
    """Validate a student's GPA."""

    try:
        gpa = float(gpa)
    except (TypeError, ValueError):
        return False, "GPA must be a number."

    if gpa < 0:
        return False, "GPA cannot be negative."

    if gpa > 4.0:
        return False, "GPA cannot be greater than 4.0."

    return True, ""


def validate_student_data(student_data):
    """Validate all student information."""

    validations = [
        ("name", validate_name),
        ("email", validate_email),
        ("course", validate_course),
        ("year_level", validate_year_level)
    ]

    for field, validator in validations:
        valid, message = validator(student_data.get(field, ""))

        if not valid:
            return False, message

    valid, message = validate_gpa(
        student_data.get("gpa", 0.0)
    )

    if not valid:
        return False, message

    return True, ""