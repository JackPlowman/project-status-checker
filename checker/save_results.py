from sqlite3 import Cursor, connect

from structlog import get_logger, stdlib

from checker.application_configuration import ApplicationConfiguration
from checker.url_check_result import URLCheckResult

logger: stdlib.BoundLogger = get_logger()


def save_results(application_configuration: ApplicationConfiguration, results: list[URLCheckResult]) -> None:
    """Save the results to a database.

    Args:
        application_configuration (ApplicationConfiguration): The application configuration.
        results (list[URLCheckResult]): The list of URL check results.
    """
    with connect(application_configuration.config_file_path) as connection:
        cursor = connection.cursor()
        create_tables_if_not_exist(cursor)


def create_tables_if_not_exist(cursor: Cursor) -> None:
    """Create the tables if they do not exist.

    Args:
        cursor (Cursor): The database cursor.
    """
    tables_created = []
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='results'")
    if cursor.fetchone() is None:
        cursor.execute("CREATE TABLE url_check_results (url TEXT, status_code INTEGER, success BOOLEAN)")
        cursor.commit()
        logger.debug("Created table url_check_results")
    if tables_created:
        logger.info("Tables created", tables=tables_created)
