from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class TestCaseWebdriver(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_case_webdriver(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        self.assertFalse(driver.find_element_by_css_selector("small.error").is_displayed())
        driver.find_element_by_xpath("//button[@type='submit']").click()
        self.assertTrue(driver.find_element_by_css_selector("small.error").is_displayed())
        driver.find_element_by_id("url").clear()
        driver.find_element_by_id("url").send_keys("http://www.cdlib.org")
        Select(driver.find_element_by_id("customDropdown1")).select_by_visible_text("Green Chilies")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("12345678A%")
        driver.find_element_by_id("confirmPassword").clear()
        driver.find_element_by_id("confirmPassword").send_keys("12345678A%")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_id("radio2").click()
        driver.find_element_by_id("checkbox1").click()
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
