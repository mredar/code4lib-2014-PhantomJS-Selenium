import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class SeleniumWebdriverTest(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox()
        caps = webdriver.DesiredCapabilities.INTERNETEXPLORER
        caps['name'] = "Code{4}lib"
        caps['platform'] = "Windows 7"
        caps['version'] = "9"
###        caps = {    'platform': 'XP',
###                                    'browserName': 'chrome',
###                                    'version':'',
###                                    'name':'TestC4lib'
###                               }
        sauce_user = os.environ.get('SAUCE_USER')
        sauce_key = os.environ.get('SAUCE_KEY')
        exe = 'http://' + sauce_user + ':' + sauce_key + '@localhost:4445/wd/hub'
        self.driver = webdriver.Remote(desired_capabilities=caps,
                command_executor=exe)
        self.driver.implicitly_wait(30)
        self.base_url = ""
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_selenium_webdriver(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        self.assertFalse(driver.find_element_by_css_selector("small.error").is_displayed())
        driver.find_element_by_xpath("//button[@type='submit']").click()
        print driver.find_element_by_css_selector("small.error")
        self.assertTrue(driver.find_element_by_css_selector("small.error").is_displayed())
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("W!12345678")
        driver.find_element_by_id("confirmPassword").clear()
        driver.find_element_by_id("confirmPassword").send_keys("W112345678")
        driver.find_element_by_id("confirmPassword").clear()
        driver.find_element_by_id("confirmPassword").send_keys("w!12345678")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("w!12345678")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_id("url").clear()
        driver.find_element_by_id("url").send_keys("http://www.cdlib.org")
        Select(driver.find_element_by_id("customDropdown1")).select_by_visible_text("Raisins")
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
