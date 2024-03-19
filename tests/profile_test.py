import time
import lorem_text
from pages.base_page import BasePage
from Locators.base_locators import UserMenu
from pages.profile_page import ProfilePage
from conftest import run
from playwright.sync_api import expect


def test_rename(run):
    page = BasePage(run)
    page.auth()
    page.go_to_link(ProfilePage.PAGE_URL)
    time.sleep(3)
    page.pw.get_by_placeholder(ProfilePage.FIRST_NAME).clear()
    expect(page.pw.locator('//span[text() = "Required"]')).to_have_text('Required', timeout=5000)
    page.pw.get_by_placeholder(ProfilePage.FIRST_NAME).fill(f'{lorem_text}')
    time.sleep(2)
    expect(page.pw.locator('//span[text()= "Should not exceed 30 characters"]')).to_be_visible()
    time.sleep(2)
    page.pw.get_by_placeholder(ProfilePage.FIRST_NAME).clear()
    page.pw.get_by_placeholder(ProfilePage.FIRST_NAME).fill('Alex')
    page.pw.locator(ProfilePage.BUTTON_SAVE).scroll_into_view_if_needed()
    page.pw.locator(ProfilePage.BUTTON_SAVE).click()
    page.pw.reload()
    expect(page.pw.locator(UserMenu().USER_BUTTON)).to_contain_text('Alex')
    page.pw.screenshot(type='jpeg', path='/Users/Ikurilin/PycharmProjects/UI_avtotest/screen.jpeg')

