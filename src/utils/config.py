import json
from pathlib import Path


# Project root directory
ROOT_DIR = Path(__file__).resolve().parent.parent.parent

# Configuration file
CONFIG_FILE = ROOT_DIR / "config" / "config.json"


def load_config():
    """Load application settings from config/config.json."""

    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as file:
            config = json.load(file)

        return config

    except FileNotFoundError:
        raise FileNotFoundError(
            f"Configuration file not found: {CONFIG_FILE}"
        )

    except json.JSONDecodeError as error:
        raise ValueError(
            f"Invalid JSON in configuration file: {error}"
        )


def get_data_file():
    """Return the configured student data file path."""

    config = load_config()
    return ROOT_DIR / config.get("data_file", "data/students.json")


def get_log_file():
    """Return the configured log file path."""

    config = load_config()
    return ROOT_DIR / config.get("log_file", "logs/app.log")


def get_log_level():
    """Return the configured logging level."""

    config = load_config()
    return config.get("log_level", "INFO")