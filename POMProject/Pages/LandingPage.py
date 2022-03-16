class LandingPage():

    def __init__(self, driver):
        self.driver = driver

        self.home_link_xpath = '//*[@id="fadein"]/header/div[2]/div/div/div/div/div[2]/nav/ul/li[1]/a'
        self.Hotels_link_xpath = '//*[@id="fadein"]/header/div[2]/div/div/div/div/div[2]/nav/ul/li[2]/a'

    def click_home(self):
        self.driver.find_element_by_xpath(self.home_link_xpath).click()

    def click_hotels(self):
        self.driver.find_element_by_xpath(self.Hotels_link_xpath).click()




