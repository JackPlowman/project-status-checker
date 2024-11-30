from os import environ

from checker.configuration import Configuration


def test_configuration() -> None:
    # Arrange
    environ["INPUT_CONFIG_FILE_PATH"] = config_file_path = "abc/def/ghi/some_file.txt"
    configuration = Configuration()
    # Assert
    assert configuration.config_file_path == config_file_path
    # Clean Up
    del environ["INPUT_CONFIG_FILE_PATH"]
