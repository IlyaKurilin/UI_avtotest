from playwright.sync_api import Page


class BasePage:

    def __init__(self, pw: Page):
        self.pw=pw


    def go_to(self):
        self.pw.goto(self.PAGE_URL)


