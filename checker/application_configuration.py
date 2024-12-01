from os import getenv
from typing import Self


class ApplicationConfiguration:
    """Configuration class to handle the checker configuration."""

    config_file_path: str
    output_file_path: str

    def __init__(self) -> None:
        """Initialize the ApplicationConfiguration class."""
        self.config_file_path = self.get_and_check_for_value("INPUT_CONFIG_FILE_PATH")
        self.output_file_path = self.get_and_check_for_value("INPUT_OUTPUT_FILE_PATH")

    def get_and_check_for_value(self: Self, key: str) -> str:
        """Get a valINPUT_OUTPUT_FILE_PATHue from the action input and check it has been set.

        Args:
            key (str): The key to get the value for.

        Returns:
            str: The value for the key or None if it is not set.
        """
        value = getenv(key)
        if isinstance(value, str):
            return value
        updated_variable_key = key.removeprefix("INPUT_") if "INPUT_" in key else key
        msg = f"{updated_variable_key} environment variable is not set"
        raise ValueError(msg)
