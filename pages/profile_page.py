from pages.base_page import BasePage
from config.links import Links


class ProfilePage(BasePage):
    PAGE_URL = Links.MY_INFO_PAGE
    FIRST_NAME = "First Name"
    MIDDLE_NAME = "name=middleName"
    LAST_NAME = "name = lastName"
    EMPLOYEE_ID = "(//input[@class='oxd-input oxd-input--active'])[2]"
    OTHER_ID = '(//input[@class="oxd-input oxd-input--active"])[3]'
    NATIONALITY = '(//i[contains(@class, "select")])[1]'
    MARITAL_STATUS = '(//i[contains(@class, "select")])[2]'
    GENDER_MALE = "//label[text()='Male']"
    GENDER_FEMALE = "//label[text()='Female']"
    BUTTON_SAVE = '(//button[@type="submit"])[1]'



