import pytest

from Locators.base_locators import MenuLoc
from pages.base_page import BasePage


# Запускает браузер для каждого из тестов
@pytest.fixture(scope="function")
def run(playwright):
    print("\nstart browser for test..")
    browser = playwright.chromium.launch(channel="chrome", headless=False)
    context = browser.new_context(ignore_https_errors=True)
    pw = context.new_page()
    yield pw
    print("\nquit browser..")
    browser.close()