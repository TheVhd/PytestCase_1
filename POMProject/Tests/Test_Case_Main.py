import time
from selenium import webdriver
import unittest
# from POMProject.Pages.Credentials import Credentials
from POMProject.Pages.LandingPage import LandingPage
from POMProject.Pages.Hotels import Hotels
from POMProject.Pages.logInCase import logInCase


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        time.sleep(1)
        cls.driver.maximize_window()

    def test_browse_hotels(self):
        driver = self.driver
        signin = logInCase(driver)
        signin.access(driver)
        print("Login Completed")

        home_page = LandingPage(driver)
        home_page.execute()
        print('Browsing Completed')

        # Select a hotel to see
        visitHotel = Hotels(driver)
        visitHotel.click_hotel()
        print('in the hotel page now')
        print('All Cases Successfully Completed')

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.close()


if __name__ == '__main__':
    unittest.main()
