import pytest

from checker.url import URL


@pytest.mark.parametrize(
    ("address", "allowed_status_code"),
    [
        ("http://www.google.com", 200),
        ("https://www.google.com", 200),
        ("http://www.google.com", 404),
        ("http://www.google.com", 500),
    ],
)
def test_url(address: str, allowed_status_code: int) -> None:
    # Act
    url = URL(address, allowed_status_code)
    # Assert
    assert url.address == address
    assert url.allowed_status_code == allowed_status_code
