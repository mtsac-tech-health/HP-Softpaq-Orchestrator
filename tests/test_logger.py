from pathlib import Path

from SoftPaqOrchestrator import logger


LOGS_FILENAME = "log_tests.log"
LOGS_PATH = Path.cwd() / "logs"

LOG_FILE_PATH = LOGS_PATH / LOGS_FILENAME


class TestLogger:
    def test_create_logger_with_file_extension(self):
        assert not LOG_FILE_PATH.exists()

        log = logger.start(LOGS_FILENAME)

        assert LOG_FILE_PATH.exists()

        del log
        LOG_FILE_PATH.unlink()

    def test_create_logger_without_file_extension(self):
        assert not LOG_FILE_PATH.exists()

        log = logger.start("log_tests")

        assert LOG_FILE_PATH.exists()

        del log
        LOG_FILE_PATH.unlink()

    def test_adding_to_log(self):
        log = logger.start(LOGS_FILENAME)

        assert LOG_FILE_PATH.stat().st_size == 0

        log.debug("Adding a test log.")

        assert LOG_FILE_PATH.stat().st_size > 0

        del log
        LOG_FILE_PATH.unlink()
