from pathlib import Path

from bs4 import BeautifulSoup
from markdown import markdown


def test_github_summary() -> None:
    # Act
    with Path("tests/github_summary/GITHUB_ACTION_SUMMARY.md").open() as file:
        summary_markdown = file.read()
    table_html = markdown(summary_markdown, extensions=["markdown.extensions.tables"])
    bs4_html = BeautifulSoup(table_html, "html.parser")
    headers = bs4_html.find_all("th")
    # Assert Headers
    headers_text = [header.text for header in headers]
    assert headers_text == ["URL Address", "Status Code", "Success"]
    # Assert row count
    rows = bs4_html.find_all("tr")
    assert len(rows) > 3
