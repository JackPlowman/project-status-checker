from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .url import URL


@dataclass
class URLCheckResult:
    """A class to represent the result of a URL check."""

    url: URL
    status_code: int
    success: bool
