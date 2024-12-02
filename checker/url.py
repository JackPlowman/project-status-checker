from dataclasses import dataclass


@dataclass
class URL:
    """URL class."""

    alias: str
    address: str
    allowed_status_code: int
