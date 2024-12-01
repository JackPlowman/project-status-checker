from sqlite3 import connect,Connection,Cursor

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
        cursor.execute("CREATE TABLE IF NOT EXISTS url_check_results (url TEXT, status_code INTEGER, success INTEGER)")
        for result in results:
            cursor.execute(
                "INSERT INTO url_check_results (url, status_code, success) VALUES (?, ?, ?)",
                (result.url.address, result.status_code, result.success),
            )
        connection.commit()
        logger.info("Results saved to database", database_path=application_configuration.config_file_path)


def create_tables_if_not_exist(cursor: Cursor) -> None:
    """Create the tables if they do not exist.

    Args:
        cursor (Cursor): The database cursor.
    """
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='url_check_results'")
    return cursor.fetchone() is not None



