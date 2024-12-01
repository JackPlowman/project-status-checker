from unittest.mock import MagicMock, patch

from checker.checker import check_urls, load_configuration_file, run_checker

FILE_PATH = "checker.checker"

@patch(f"{FILE_PATH}.generate_action_summary")
@patch(f"{FILE_PATH}.save_results")
@patch(f"{FILE_PATH}.check_urls")
@patch(f"{FILE_PATH}.load_configuration_file")
@patch(f"{FILE_PATH}.ApplicationConfiguration")
@patch(f"{FILE_PATH}.set_up_custom_logging")
def test_run_checker(
    mock_set_up_custom_logging: MagicMock,
    mock_application_configuration: MagicMock,
    load_configuration_file: MagicMock,
    mock_check_urls: MagicMock,
    mock_save_results: MagicMock,
    mock_generate_action_summary: MagicMock,
) -> None:
    """Test the run_checker function."""
    # Act
    run_checker()
    # Assert
    mock_set_up_custom_logging.assert_called_once_with()
    mock_application_configuration.assert_called_once_with()
    load_configuration_file.assert_called_once_with(mock_application_configuration.return_value)
    mock_check_urls.assert_called_once_with(load_configuration_file.return_value)
    mock_save_results.assert_called_once_with(mock_application_configuration.return_value, mock_check_urls.return_value)
    mock_generate_action_summary.assert_called_once_with(mock_check_urls.return_value)


@patch(f"{FILE_PATH}.Path.exists", return_value=True)
@patch(f"{FILE_PATH}.Path.open", new_callable=MagicMock)
@patch(f"{FILE_PATH}.load")
def test_load_configuration_file(mock_load: MagicMock, mock_open: MagicMock, mock_exists: MagicMock) -> None:
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
    mock_exists.assert_called()


@patch(f"{FILE_PATH}.get")
def test_check_urls(mock_get: MagicMock) -> None:
    """Test the check_urls function."""
    # Arrange
    mock_url = MagicMock()
    mock_url.address = "http://example.com"
    mock_url.allowed_status_code = 200

    mock_response = MagicMock()
    mock_response.status_code = 200

    mock_get.return_value = mock_response

    # Act
    results = check_urls([mock_url])

    # Assert
    assert len(results) == 1
    assert results[0].url == mock_url
    assert results[0].status_code == 200
    assert results[0].success is True
    mock_get.assert_called_once_with(mock_url.address, timeout=1)
