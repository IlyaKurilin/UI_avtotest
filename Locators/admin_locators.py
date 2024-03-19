from base_locators import MenuLoc


class AdminLoc(MenuLoc):
    def __init__(self):
        super().__init__()
        self.USER_MANAGEMENT = '//span[text()="User Management "]'
        self.USER = '//a[@role="menuitem"]'
        self.JOB = '//a[@role="Job "]'


class Job(AdminLoc):
    def __init__(self):
        super().__init__()
        self.JOB_TITLES = '(//a[@href="#"])[0]'
        self.Pay_Grades = '(//a[@href="#"])[1]'
        self.Employment_Status = '(//a[@href="#"])[2]'
        self.Job_Categories = '(//a[@href="#"])[3]'
        self.Work_Shifts = '(//a[@href="#"])[4]'
