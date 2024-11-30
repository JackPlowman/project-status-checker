from os import environ, getenv
from pathlib import Path

from structlog import get_logger, stdlib

from checker.url_check_result import URLCheckResult

logger: stdlib.BoundLogger = get_logger()


def generate_action_summary(_results: list[URLCheckResult]) -> None:
    """Generate the action summary.

    Args:
        results (list[URLCheckResult]): The list of URL check results.
    """
    if getenv("GITHUB_ACTION", "false") == "false":
        logger.debug("Not running in GitHub Actions, skipping generating action summary")
        return
    logger.debug("Generating action summary")
    with Path(environ["GITHUB_STEP_SUMMARY"]).open("w") as file:
        file.write("")
