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
    assert len(rows) == 2
    # Assert row contents
    row1 = rows[1]
    row1_data = row1.find_all("td")
    row1_data_text = [data.text for data in row1_data]
    assert row1_data_text == ["https://www.google.com", "200", "True"]
