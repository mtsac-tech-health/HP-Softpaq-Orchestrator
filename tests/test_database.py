from time import sleep
from pathlib import Path

import pytest

from SoftPaqOrchestrator.database import Database, DatabaseCreationError


class TestDatabase:
    def test_database_creation_error(self):
        database_file = Path.cwd() / "database" / "tests.db"
        create_db_sql_file = Path.cwd() / "tests" / "create_db_WITH_ERRORS.sql"

        with pytest.raises(DatabaseCreationError):
            Database(database_file, create_db_sql_file)
            sleep(0.2)

        assert Path.exists(database_file) is False

    def test_database_creation_no_error(self):
        database_file = Path.cwd() / "database" / "tests.db"

        try:
            Database(database_file=database_file)
            sleep(0.2)
        except Exception as exc:
            assert False, f"Creating the database raised an exception {exc}"

        assert Path.exists(database_file)

        database_file.unlink()
