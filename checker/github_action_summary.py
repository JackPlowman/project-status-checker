from os import environ, getenv
from pathlib import Path

from mdutils.mdutils import MdUtils
from structlog import get_logger, stdlib

from checker.url_check_result import URLCheckResult

logger: stdlib.BoundLogger = get_logger()


def generate_action_summary(results: list[URLCheckResult]) -> None:
    """Generate the action summary.

    Args:
        results (list[URLCheckResult]): The list of URL check results.
    """
    if getenv("GITHUB_ACTION", "false") == "false":
        logger.debug(
            "Not running in GitHub Actions, skipping generating action summary"
        )
        return
    logger.debug("Generating action summary")
    # Generate the markdown contents
    markdown_file = MdUtils(file_name="markdown.md", title="GitHub Action Summary")
    table_headers = ["URL Address", "Status Code", "Success"]
    list_of_strings = [*table_headers]
    for result in results:
        list_of_strings.extend([result.url.address, result.status_code, result.success])
    markdown_file.new_table(
        columns=len(table_headers),
        rows=int(len(list_of_strings) / len(table_headers)),
        text=list_of_strings,
        text_align="center",
    )
    # Write the markdown contents to the file
    with Path(environ["GITHUB_STEP_SUMMARY"]).open("w") as file:
        file.write(markdown_file.get_md_text())
