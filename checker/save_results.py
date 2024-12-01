from sqlite3 import Cursor, connect

from structlog import get_logger, stdlib

from checker.application_configuration import ApplicationConfiguration
from checker.url_check_result import URLCheckResult

logger: stdlib.BoundLogger = get_logger()


def save_results(application_configuration: ApplicationConfiguration, _results: list[URLCheckResult]) -> None:
    """Save the results to a database.

    Args:
        application_configuration (ApplicationConfiguration): The application configuration.
        results (list[URLCheckResult]): The list of URL check results.
    """
    with connect(application_configuration.output_file_path) as connection:
        cursor = connection.cursor()
        create_tables_if_not_exist(cursor)
        connection.commit()

def create_tables_if_not_exist(cursor: Cursor) -> None:
    """Create the tables if they do not exist.

    Args:
        cursor (Cursor): The database cursor.
    """
    tables_created = []
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='url'")
    if cursor.fetchone() is None:
        logger.debug("Creating table url")
        cursor.execute("CREATE TABLE url (url_id INTEGER PRIMARY KEY, alias TEXT NOT NULL, url TEXT NOT NULL)")
        logger.debug("Created table results")
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='results'")
    if cursor.fetchone() is None:
        logger.debug("Creating table results")
        cursor.execute(
            "CREATE TABLE results ("
            "result_id INTEGER PRIMARY KEY, "
            "url_id INTEGER NOT NULL, "
            "success BOOLEAN NOT NULL, "
            "date_time_stamp TEXT NOT NULL, "
            "FOREIGN KEY (url_id) REFERENCES urls (url_id))"
        )
        logger.debug("Created table results")
    if tables_created:
        logger.info("Tables created", tables=tables_created)
