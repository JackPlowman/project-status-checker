from unittest.mock import MagicMock, patch

from checker.checker import load_configuration_file, run_checker

FILE_PATH = "checker.checker"


@patch(f"{FILE_PATH}.load_configuration_file")
@patch(f"{FILE_PATH}.ApplicationConfiguration")
@patch(f"{FILE_PATH}.set_up_custom_logging")
def test_run_checker(
    mock_set_up_custom_logging: MagicMock, mock_application_configuration: MagicMock, load_configuration_file: MagicMock
) -> None:
    """Test the run_checker function."""
    # Act
    run_checker()
    # Assert
    mock_set_up_custom_logging.assert_called_once_with()
    mock_application_configuration.assert_called_once_with()
    load_configuration_file.assert_called_once()


@patch(f"{FILE_PATH}.Path.open", new_callable=MagicMock)
@patch(f"{FILE_PATH}.load")
def test_load_configuration_file(mock_load: MagicMock, mock_open: MagicMock) -> None:
    """Test the load_configuration_file function."""
    mock_file_contents = {
        "urls": [
            {"url": "http://example.com", "allowed_status_code": 200},
            {"url": "http://example.org", "allowed_status_code": 404},
        ]
    }
    mock_load.return_value = mock_file_contents
    mock_open.return_value.__enter__.return_value = MagicMock()

    mock_application_configuration = MagicMock()
    mock_application_configuration.config_file_path = "dummy_path"

    # Act
    urls = load_configuration_file(mock_application_configuration)

    # Assert
    assert len(urls) == 2
    assert urls[0].address == "http://example.com"
    assert urls[0].allowed_status_code == 200
    assert urls[1].address == "http://example.org"
    assert urls[1].allowed_status_code == 404
    mock_open.assert_called_once_with()
    mock_load.assert_called_once_with(mock_open.return_value.__enter__.return_value)
