from os import environ

from checker.application_configuration import ApplicationConfiguration


def test_application_configuration() -> None:
    # Arrange
    environ["INPUT_CONFIG_FILE_PATH"] = config_file_path = "abc/def/ghi/some_file.txt"
    configuration = ApplicationConfiguration()
    # Assert
    assert configuration.config_file_path == config_file_path
    # Clean Up
    del environ["INPUT_CONFIG_FILE_PATH"]
