from os import environ

from checker.application_configuration import ApplicationConfiguration


def test_application_configuration() -> None:
    # Arrange
    environ["INPUT_CONFIG_FILE_PATH"] = config_file_path = "abc/def/ghi/some_file.txt"
    environ["INPUT_OUTPUT_FILE_PATH"] = output_file_path = "jkl/mno/pqr/some_output_file.txt"
    configuration = ApplicationConfiguration()
    # Assert
    assert configuration.config_file_path == config_file_path
    assert configuration.output_file_path == output_file_path
    # Clean Up
    del environ["INPUT_CONFIG_FILE_PATH"]
    del environ["INPUT_OUTPUT_FILE_PATH"]
