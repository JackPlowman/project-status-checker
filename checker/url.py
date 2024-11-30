from dataclasses import dataclass


@dataclass
class URL:
    """URL class."""
    address: str
    allowed_status_code:int

