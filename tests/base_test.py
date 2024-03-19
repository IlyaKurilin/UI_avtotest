import time
import playwright
import pytest

from config.links import Links
from playwright.sync_api import expect, Page
from pages.base_page import BasePage
from conftest import run
from Locators.base_locators import MenuLoc, UserMenu
from pages.login_page import LoginPage


@pytest.mark.menu_button
def test_admin_button(run):
    page = BasePage(run)
    page.auth()
    menu_loc = MenuLoc()
    page.pw.locator(menu_loc.ADMIN).click()
    assert page.pw.url == Links.ADMIN_PAGE
    expect(page.pw.locator('//h5')).to_have_text('System Users')


@pytest.mark.menu_button
def test_pim_button(run):
    page = BasePage(run)
    page.auth()
    menu_loc = MenuLoc()
    page.pw.locator(menu_loc.PIM).click()
    assert page.pw.url == Links.PIM_PAGE
    expect(page.pw.locator('//h6')).to_have_text('PIM')


@pytest.mark.menu_button
def test_leave_button(run):
    page = BasePage(run)
    page.auth()
    menu_loc = MenuLoc()
    page.pw.locator(menu_loc.LEAVE).click()
    assert page.pw.url == Links.LEAVE_PAGE
    expect(page.pw.locator('//h5')).to_have_text('Leave List')


@pytest.mark.menu_rout_button
def test_time_button(run):
    page = BasePage(run)
    page.auth()
    menu_loc = MenuLoc()
    page.pw.locator(menu_loc.TIME)
    assert page.pw.url == Links.TIME_PAGE
    expect(page.pw.locator('//h6[2]')).to_have_text('Timesheets')


def test_logout(run):
    page = BasePage(run)
    page.auth()
    user_menu = UserMenu()
    page.pw.locator(user_menu.USER_BUTTON).click()
    page.pw.locator(user_menu.LOGOUT).click()
    expect(page.pw.locator('//h5')).to_have_text('Login')
    expect(page.pw.locator("//input[@name='username']")).to_be_empty()
    expect(page.pw.locator('//input[@name="password"]')).to_be_empty()
