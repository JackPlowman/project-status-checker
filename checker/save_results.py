from datetime import UTC, datetime
from sqlite3 import Connection, Cursor, connect

from structlog import get_logger, stdlib

from checker.application_configuration import ApplicationConfiguration
from checker.url_check_result import URLCheckResult

logger: stdlib.BoundLogger = get_logger()


def save_results(
    application_configuration: ApplicationConfiguration, results: list[URLCheckResult]
) -> None:
    """Save the results to a database.

    Args:
        application_configuration (ApplicationConfiguration):
            The application configuration.
        results (list[URLCheckResult]): The list of URL check results.
    """
    with connect(application_configuration.database_file_path) as connection:
        cursor = connection.cursor()
        create_tables_if_not_exist(connection, cursor)
        for result in results:
            update_results_table(result, connection, cursor)


def update_results_table(
    result: URLCheckResult, connection: Connection, cursor: Cursor
) -> None:
    """Update the results table with the URL check result.

    Args:
        result (URLCheckResult): The URL check result.
        connection (Connection): The database connection.
        cursor (Cursor): The database cursor.
    """
    # Check if the URL is already in the database
    cursor.execute("SELECT url_id FROM url WHERE url = ?", (result.url.address,))
    url_id = cursor.fetchone()
    # If the URL is not in the database, add it
    if url_id is None:
        cursor.execute(
            "INSERT INTO url (alias, url) VALUES (?, ?)",
            (result.url.alias, result.url.address),
        )
        cursor.execute("SELECT url_id FROM url WHERE url = ?", (result.url.address,))
        url_id = cursor.fetchone()
    # Add the result to the results table
    cursor.execute(
        "INSERT INTO results (url_id, success, date_time_stamp) VALUES (?, ?, ?)",
        (url_id[0], result.success, datetime.now(UTC)),
    )
    # Commit the changes
    connection.commit()


def create_tables_if_not_exist(connection: Connection, cursor: Cursor) -> None:
    """Create the tables if they do not exist.

    Args:
        connection (Connection): The database connection.
        cursor (Cursor): The database cursor.
    """
    tables_created = []
    # Check if url table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='url'")
    if cursor.fetchone() is None:
        logger.debug("Creating table url")
        cursor.execute(
            "CREATE TABLE url (url_id INTEGER PRIMARY KEY, "
            "alias TEXT NOT NULL, url TEXT NOT NULL)"
        )
        logger.debug("Created table url")
        tables_created.append("url")
        # Check if results table exists
    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='results'"
    )
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
        tables_created.append("results")
    if tables_created:
        logger.info("Tables created", tables=tables_created)
        connection.commit()
