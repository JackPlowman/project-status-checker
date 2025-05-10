from os import environ

from checker.application_configuration import ApplicationConfiguration


def test_application_configuration() -> None:
    # Arrange
    github_workspace = "github/workspace/"
    environ["INPUT_CONFIG_FILE_PATH"] = config_file_path = "abc/def/ghi/some_file.txt"
    environ["INPUT_DATABASE_FILE_PATH"] = database_file_path = (
        "jkl/mno/pqr/some_database_file.txt"
    )
    configuration = ApplicationConfiguration()
    # Assert
    assert configuration.config_file_path == f"{github_workspace}{config_file_path}"
    assert configuration.database_file_path == f"{github_workspace}{database_file_path}"
    # Clean Up
    del environ["INPUT_CONFIG_FILE_PATH"]
    del environ["INPUT_DATABASE_FILE_PATH"]
