import pytest
import playwright as pw

@pytest.fixture(scope="function", autouse=True)
def run(playwright):
    print("\nstart browser for test..")
    browser = playwright.chromium.launch(channel="chrome", headless=True)
    context = browser.new_context(ignore_https_errors=True)
    pw = context.new_page()
    yield pw
    print("\nquit browser..")
    browser.close()