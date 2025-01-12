from os import environ
from unittest.mock import MagicMock, patch

from checker.github_action_summary import generate_action_summary
from checker.url import URL
from checker.url_check_result import URLCheckResult

FILE_PATH = "checker.github_action_summary"


@patch(f"{FILE_PATH}.getenv", return_value="true")
@patch(f"{FILE_PATH}.Path.open", new_callable=MagicMock)
def test_generate_action_summary(mock_open: MagicMock, _mock_getenv: MagicMock) -> None:
    """Test the generate_action_summary function."""
    # Arrange
    environ["GITHUB_STEP_SUMMARY"] = "dummy_path"
    url1 = URL("example1", "http://example.com", 200)
    url2 = URL("example2", "http://example.org", 404)
    result1 = URLCheckResult(url1, 200, True)  # noqa: FBT003
    result2 = URLCheckResult(url2, 404, True)  # noqa: FBT003
    results = [result1, result2]
    mock_file = MagicMock()
    mock_open.return_value.__enter__.return_value = mock_file
    # Act
    generate_action_summary(results)
    # Assert
    mock_open.assert_called_once_with("w")
    written_content = mock_file.write.call_args[0][0]
    assert written_content == (
        "\nGitHub Action Summary\n=====================\n\n"
        "|URL Address|Status Code|Success|\n| :---: | :---: | :---: |\n"
        "|http://example.com|200|True|\n|http://example.org|404|True|\n"
    )
    # Clean up
    del environ["GITHUB_STEP_SUMMARY"]


@patch(f"{FILE_PATH}.getenv", return_value="false")
def test_generate_action_summary_not_in_github_actions(mock_getenv: MagicMock) -> None:
    """Test the generate_action_summary function when not in GitHub Actions."""
    # Arrange
    results = []
    # Act
    generate_action_summary(results)
    # Assert
    mock_getenv.assert_called_once_with("GITHUB_ACTION", "false")
