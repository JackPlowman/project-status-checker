from os import getenv
from typing import Self


class ApplicationConfiguration:
    """Configuration class to handle the checker configuration."""

    config_file_path: str
    database_file_path: str

    def __init__(self) -> None:
        """Initialize the ApplicationConfiguration class."""
        config_file_path = self.get_and_check_for_value("INPUT_CONFIG_FILE_PATH")
        self.config_file_path = (
            config_file_path
            if "github/workspace" in config_file_path
            else f"github/workspace/{config_file_path}"
        )
        database_file_path = self.get_and_check_for_value("INPUT_DATABASE_FILE_PATH")
        self.database_file_path = (
            database_file_path
            if "github/workspace" in database_file_path
            else f"github/workspace/{database_file_path}"
        )

    def get_and_check_for_value(self: Self, key: str) -> str:
        """Get a value from the action input and check it has been set.

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
