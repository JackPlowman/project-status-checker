from json import load
from pathlib import Path

from requests import get
from requests.exceptions import RequestException
from structlog import get_logger, stdlib

from checker.application_configuration import ApplicationConfiguration
from checker.custom_logging import set_up_custom_logging
from checker.url import URL
from checker.url_check_result import URLCheckResult

logger: stdlib.BoundLogger = get_logger()


def run_checker() -> None:
    """Run the checker."""
    set_up_custom_logging()
    configuration = ApplicationConfiguration()
    urls = load_configuration_file(configuration)
    check_urls(urls)


def load_configuration_file(application_configuration: ApplicationConfiguration) -> list[URL]:
    """Load the configuration."""
    with Path(application_configuration.config_file_path).open() as file:
        file_contents = load(file)
    logger.debug("Loaded configuration file", file_contents=file_contents)
    return [URL(url["url"], url["allowed_status_code"]) for url in file_contents["urls"]]

def check_urls(urls: list[URL]) -> list[URLCheckResult]:
    """Check the URLs."""
    results = []
    for url in urls:
        try:
            logger.debug("Checking URL", url=url)
            response = get(url.address, timeout=1)
            results.append(URLCheckResult(url, response.status_code, response.status_code == url.allowed_status_code))
        except RequestException:
            logger.exception("Failed to check URL", url=url)
    return results

