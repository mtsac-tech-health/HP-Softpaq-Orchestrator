import sqlite3
from pathlib import Path

from SoftpaqOrchestrator import logger

DATABASE_PATH = Path.cwd() / "database"
DATABASE_FILE = DATABASE_PATH / "HPSO.db"
CRATE_DB_SQL_FILE = DATABASE_PATH / "create_db.sql"


log = logger.start("database")


class Database:
    def __init__(
        self,
        database_file: Path = DATABASE_FILE,
        create_db_sql_file: Path = CRATE_DB_SQL_FILE,
    ) -> None:
        self.database_file = database_file
        self.create_db_sql_file = create_db_sql_file

        if not self._does_db_exist():
            log.debug("Database does not exist.")
            self._create_db()

    def _does_db_exist(self) -> bool:
        return Path.exists(self.database_file)

    def _create_db(self) -> None:
        log.debug(f"Creating database: {self.database_file}")
        connection = sqlite3.connect(self.database_file)

        with open(self.create_db_sql_file, "r") as file:
            sql_script = file.read()

        try:
            with connection:
                connection.executescript(sql_script)
        except sqlite3.OperationalError:
            log.exception("Could not run SQL script.")
            log.debug("Deleting database file.")

            connection.close()
            self.database_file.unlink()

            raise DatabaseCreationError
        else:
            log.debug("Database created successfully.")
            connection.close()

        del connection


class DatabaseCreationError(Exception):
    pass
