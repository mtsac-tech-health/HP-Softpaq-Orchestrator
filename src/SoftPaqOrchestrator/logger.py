import logging
from enum import Enum
from pathlib import Path

LOGS_PATH = Path.cwd() / "logs"
FILE_SUFFIX = ".log"
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"


class LoggingLevel(Enum):
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL
    FATAL = logging.FATAL


def start(
    log_filename: str, logging_level: LoggingLevel = LoggingLevel.DEBUG
) -> logging.Logger:
    if log_filename.endswith(FILE_SUFFIX):
        log_filename = log_filename[:-4]

    logger = logging.getLogger(log_filename)

    formatter = logging.Formatter(LOG_FORMAT)

    handler = logging.FileHandler(str(LOGS_PATH / (log_filename + FILE_SUFFIX)))
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    logger.setLevel(logging_level.value)

    return logger
