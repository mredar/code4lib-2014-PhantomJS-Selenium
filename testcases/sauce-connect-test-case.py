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
        caps['platform'] = "Windows XP"
        caps['version'] = "7"
###        caps = {    'platform': 'XP',
###                                    'browserName': 'chrome',
###                                    'version':'',
###                                    'name':'TestC4lib'
###                               }
        #self.driver = webdriver.Remote(desired_capabilities=desired_caps,
        #        command_executor='http://cdl-dsc:08a884ba-fbba-40ea-be77-e00786f37166@ondemand.saucelabs.com:80/wd/hub')
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
        #driver.get(self.base_url + "file:///C:/Users/mark/Dropbox/Projects/code4lib/foundation/code4lib-sample.html")
        driver.get("http://127.0.0.1:8000/")
        self.assertFalse(driver.find_element_by_css_selector("small.error").is_displayed())
        driver.find_element_by_xpath("//button[@type='submit']").click()
        print driver.find_element_by_css_selector("small.error")
        self.assertEqual(driver.find_element_by_css_selector("small.error").text, "Passwords must be at least 8 characters with 1 capital letter, 1 number, and one special character.x")
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
        driver.find_element_by_id("checkbox1").click()
        driver.find_element_by_id("radio2").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
    
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
