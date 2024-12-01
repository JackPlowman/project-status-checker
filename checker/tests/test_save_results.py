from unittest.mock import MagicMock, patch

from checker.application_configuration import ApplicationConfiguration
from checker.save_results import create_tables_if_not_exist, save_results
from checker.url_check_result import URLCheckResult

FILE_PATH = "checker.save_results"


@patch(f"{FILE_PATH}.connect")
def test_save_results(mock_connect: MagicMock) -> None:
    """Test the save_results function."""
    # Arrange
    mock_connection = mock_connect.return_value.__enter__.return_value
    mock_cursor = mock_connection.cursor.return_value
    mock_application_configuration = MagicMock(spec=ApplicationConfiguration)
    mock_application_configuration.output_file_path = "dummy_path"
    mock_results = [
        MagicMock(spec=URLCheckResult),
        MagicMock(spec=URLCheckResult),
    ]
    # Act
    save_results(mock_application_configuration, mock_results)
    # Assert
    mock_connect.assert_called_once_with("dummy_path")
    mock_connection.cursor.assert_called_once_with()
    mock_cursor.execute.assert_any_call("SELECT name FROM sqlite_master WHERE type='table' AND name='url'")
    mock_cursor.execute.assert_any_call("SELECT name FROM sqlite_master WHERE type='table' AND name='results'")
    mock_connection.commit.assert_called_once_with()


def test_create_tables_if_not_exist() -> None:
    """Test the create_tables_if_not_exist function."""
    # Arrange
    mock_cursor = MagicMock()
    # Simulate no tables existing
    mock_cursor.fetchone.side_effect = [None, None]
    # Act
    create_tables_if_not_exist(mock_cursor)
    # Assert
    mock_cursor.execute.assert_any_call("SELECT name FROM sqlite_master WHERE type='table' AND name='url'")
    mock_cursor.execute.assert_any_call(
        "CREATE TABLE url (url_id INTEGER PRIMARY KEY, alias TEXT NOT NULL, url TEXT NOT NULL)"
    )
    mock_cursor.execute.assert_any_call("SELECT name FROM sqlite_master WHERE type='table' AND name='results'")
    mock_cursor.execute.assert_any_call(
        "CREATE TABLE results ("
        "result_id INTEGER PRIMARY KEY, "
        "url_id INTEGER NOT NULL, "
        "success BOOLEAN NOT NULL, "
        "date_time_stamp TEXT NOT NULL, "
        "FOREIGN KEY (url_id) REFERENCES urls (url_id))"
    )
