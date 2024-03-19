import time

from playwright.sync_api import Page
from Locators.base_locators import Login


class BasePage:
    def __init__(self, pw: Page):
        self.domain = f'https://opensource-demo.orangehrmlive.com/web/index.php'
        self.pw = pw

    def auth(self):
        locators = Login()
        self.pw.goto(f'{self.domain}/auth/login')
        self.pw.get_by_placeholder(locators.LOGIN_INPUT).fill('Admin')
        self.pw.get_by_placeholder(locators.PASSWORD_INPUT).fill('admin123')
        self.pw.locator(locators.SUBMIT).click()
        assert self.pw.title() == 'OrangeHRM'
        time.sleep(5)

    def go_to_link(self, link):
        self.pw.goto(link)
