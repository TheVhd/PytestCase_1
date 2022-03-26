from POMProject.Pages.Credentials import Credentials


class logInCase():

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.phptravels.net/login")
        self.login = Credentials(driver)

    def access(self, driver):
        self.login.enter_username("user@phptravels.com")
        self.login.enter_password("demouser")
        self.login.click_login()
