class Credentials():

    def __init__(self, driver):
        self.driver = driver
        self.username_path = '//*[@id="fadein"]/div[1]/div/div[2]/div[2]/div/form/div[1]/div/input'
        self.password_path = '//*[@id="fadein"]/div[1]/div/div[2]/div[2]/div/form/div[2]/div[1]/input'
        self.login_button_xpath = '//*[@id="fadein"]/div[1]/div/div[2]/div[2]/div/form/div[3]/button'

    def enter_username(self, username):
        self.driver.find_element_by_xpath(self.username_path).clear()
        self.driver.find_element_by_xpath(self.username_path).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_xpath(self.password_path).clear()
        self.driver.find_element_by_xpath(self.password_path).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()


