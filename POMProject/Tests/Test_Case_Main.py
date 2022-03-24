import time
from selenium import webdriver
import unittest
from POMProject.Pages.Credentials import Credentials
from POMProject.Pages.LandingPage import LandingPage
from POMProject.Pages.Hotels import Hotels


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        time.sleep(1)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://www.phptravels.net/login")

        # login to the system
        login = Credentials(driver)
        login.enter_username("user@phptravels.com")
        login.enter_password("demouser")
        login.click_login()
        print("Login Completed")

        # Browse the page and go to the Hotels Page
        home_page = LandingPage(driver)
        home_page.click_home()
        home_page.click_hotels()
        print('Browsing Completed')

        # Select a hotel to see
        visitHotel = Hotels(driver)
        visitHotel.click_hotel()
        print('in the hotel page now')
        visitHotel.pickOne()
        print('picked a tariff')
        visitHotel.bookNow()
        print('Time to payout')

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.close()


if __name__ == '__main__':
    unittest.main()

    # self.driver.find_element_by_name("email").send_keys("user@phptravels.com")
    # self.driver.find_element_by_name("password").send_keys("demouser")
    # self.driver.find_element_by_xpath('//*[@id="fadein"]/div[1]/div/div[2]/div[2]/div/form/div[3]/button').click()
