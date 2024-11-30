from json import load
from pathlib import Path

from structlog import get_logger, stdlib

from checker.application_configuration import ApplicationConfiguration
from checker.custom_logging import set_up_custom_logging
from checker.url import URL

logger: stdlib.BoundLogger = get_logger()


def run_checker() -> None:
    """Run the checker."""
    set_up_custom_logging()
    configuration = ApplicationConfiguration()
    urls = load_configuration_file(configuration)
    logger.warning("Loaded configuration", urls=urls)


def load_configuration_file(application_configuration: ApplicationConfiguration) -> list[URL]:
    """Load the configuration."""
    with Path(application_configuration.config_file_path).open() as file:
        file_contents = load(file)
    logger.debug("Loaded configuration file", file_contents=file_contents)
    return [URL(url["url"], url["allowed_status_code"]) for url in file_contents["urls"]]
