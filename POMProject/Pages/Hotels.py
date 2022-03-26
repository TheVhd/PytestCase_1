import time


class Hotels():

    def __init__(self, driver):
        self.driver = driver
        self.nextButton = '//*[@id="fadein"]/section[2]/div/div[2]/div/div/div/div[2]/div[2]/i'
        self.selectHotel = '//*[@id="fadein"]/section[2]/div/div[2]/div/div/div/div[1]/div/div[8]/div/div[1]/a/img'
        self.choose = '//*[@id="availability"]/div[2]/div[4]/div[2]/div/div[2]/form/div/div[3]/div/select/option[2]'
        self.bookNow = '//*[@id="availability"]/div[2]/div[4]/div[2]/div/div[2]/form/div/div[4]/div/div/button'

    def click_hotel(self):
        time.sleep(2.0)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element_by_xpath(self.nextButton).click()
        self.driver.find_element_by_xpath(self.selectHotel).click()
        self.driver.find_element_by_xpath(self.choose).click()
        print('picked a tariff')
        time.sleep(4.0)
        self.driver.find_element_by_xpath(self.bookNow).click()
        print('Time to payout')
        time.sleep(4.0)
