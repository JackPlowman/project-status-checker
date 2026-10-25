from dataclasses import dataclass

from .url import URL


@dataclass
class URLCheckResult:
    """A class to represent the result of a URL check."""

    url: URL
    status_code: int
    success: bool
