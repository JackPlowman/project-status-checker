import pytest

from checker.url import URL


@pytest.mark.parametrize(
    ("alias", "address", "allowed_status_code"),
    [
        ("google1", "http://www.google.com", 200),
        ("google2", "https://www.google.com", 200),
        ("google3", "http://www.google.com", 404),
        ("google4", "http://www.google.com", 500),
    ],
)
def test_url(alias: str, address: str, allowed_status_code: int) -> None:
    # Act
    url = URL(alias, address, allowed_status_code)
    # Assert
    assert url.address == address
    assert url.allowed_status_code == allowed_status_code
