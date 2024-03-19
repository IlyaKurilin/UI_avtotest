
class Login:
    def __init__(self):
        self.LOGIN_INPUT = 'Username'
        self.PASSWORD_INPUT = 'Password'
        self.SUBMIT = '//button[@type = "submit"]'

class MenuLoc:
    def __init__(self):
        self.MENU_BUTTON = '//i[contains(@class, "oxd-icon bi-list ")]' #в мобильной версии
        self.PROFILE = '//span[@class = "oxd-userdropdown-tab"]'
        self.SEARCH_INPUT = '//input[@placeholder="Search"]'
        self.ADMIN = '//a[contains(@href, "AdminModule")]'
        self.PIM = '//a[contains(@href, "PimModule")]'
        self.LEAVE = "//span[text()='Leave']"
        self.TIME = "//span[text()='Time']"
        self.RECRUITMENT = "//span[text()='Recruitment']"
        self.MY_INFO = "//span[text()='MyInfo']"
        self.PERFORMANCE = "//span[text()='Performance']"
        self.DASHBOARD = "//span[text()='Dashboard']"
        self.DIRECTORY = "//span[text()='Directory']"
        self.MAINTENANCE = "//span[text()='Maintenance']"
        self.CLAIM = "//span[text()='Claim']"
        self.BUZZ = "//span[text()='Buzz']"

class UserMenu():
    def __init__(self):
        self.USER_BUTTON = '//p[@class="oxd-userdropdown-name"]'
        self.ABOUT_BUTTON = "//a[text()='About']"
        self.SUPPORT_BUTTON = "//a[text()='Support']"
        self.CHANGE_PASSWORD = "//a[text()='Change Password']"
        self.LOGOUT = "//a[text()='Logout']"