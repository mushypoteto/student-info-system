import logging
from logging.handlers import RotatingFileHandler

from src.utils.config import get_log_file, get_log_level


def setup_logger():
    """Configure application-wide logging."""

    log_file = get_log_file()
    log_file.parent.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger("StudentInformationSystem")

    # Prevent duplicate handlers
    if logger.handlers:
        return logger

    log_level = getattr(
        logging,
        get_log_level().upper(),
        logging.INFO
    )

    logger.setLevel(log_level)

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    # File logging
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=1_000_000,
        backupCount=3,
        encoding="utf-8"
    )

    file_handler.setFormatter(formatter)

    # Console logging
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger