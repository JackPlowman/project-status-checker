from os import getenv


class Configuration:
    """Configuration class to handle the checker configuration."""
    config_file_path:str

    def __init__(self) -> None:
        """Initialize the Configuration class."""
        self.config_file_path = getenv("INPUT_CONFIG_FILE_PATH")
