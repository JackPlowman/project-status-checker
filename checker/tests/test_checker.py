from unittest.mock import MagicMock, patch

from checker.checker import run_checker

FILE_PATH = "checker.checker"


@patch(f"{FILE_PATH}.set_up_custom_logging")
def test_run_checker(mock_set_up_custom_logging: MagicMock) -> None:
    """Test the run_checker function."""
    # Act
    run_checker()
    # Assert
    mock_set_up_custom_logging.assert_called_once_with()
