from typing import get_type_hints

import pytest

from checker.url import URL
from checker.url_check_result import URLCheckResult


def test_result_annotations_are_resolvable() -> None:
    assert get_type_hints(URLCheckResult)["url"] is URL


@pytest.mark.parametrize(
    ("alias", "url_address", "status_code", "success"),
    [
        ("example1", "http://example.com", 200, True),
        ("example2", "http://example.com", 404, False),
    ],
)
def test_url_check_result(
    alias: str, url_address: str, status_code: int, success: bool
) -> None:
    # Arrange
    url = URL(alias, url_address, status_code)
    # Act
    result = URLCheckResult(url, status_code, success)
    # Assert
    assert result.url == url
    assert result.status_code == status_code
    assert result.success == success
