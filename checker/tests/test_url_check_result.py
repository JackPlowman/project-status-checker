
import pytest

from checker.url import URL
from checker.url_check_result import URLCheckResult


@pytest.mark.parametrize(("url_address", "status_code", "success"), [
    ("http://example.com", 200, True),
    ("http://example.com", 404, False),
])
def test_url_check_result(url_address: str, status_code: int, success: bool) -> None:  # noqa: FBT001
    # Arrange
    url = URL(url_address, status_code)
    # Act
    result = URLCheckResult(url, status_code, success)
    # Assert
    assert result.url == url
    assert result.status_code == status_code
    assert result.success == success
