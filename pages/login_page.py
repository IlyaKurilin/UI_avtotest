from pages.base_page import BasePage
from config.links import Links


class LoginPage(BasePage):
    PAGE_URL = Links.LOGINING_PAGE

    USERNAME = 'name=username'
    PASSWORD = 'name = password'
    SUBMIT = "//button[@type='submit']"

    def __init__(self, pw):
        super().__init__(pw)
        self.page = pw

    def logining(self, login, password):
        self.page.locator(self.USERNAME).fill(login)
        self.page.locator(self.PASSWORD).fill(password)
        self.page.locator(self.SUBMIT).click()
