require "json"
require "selenium-webdriver"
gem "test-unit"
require "test/unit"

class TestCase < Test::Unit::TestCase

  def setup
    @driver = Selenium::WebDriver.for :phantomjs
    @base_url = "http://localhost:8000/"
    @accept_next_alert = true
    @driver.manage.timeouts.implicit_wait = 30
    @verification_errors = []
  end
  
  def teardown
    @driver.quit
    assert_equal [], @verification_errors
  end
  
  def test_case
    @driver.get(@base_url + "/")
    assert_false @driver.find_element(:css, "small.error").displayed?
    @driver.find_element(:xpath, "//button[@type='submit']").click
    assert_true @driver.find_element(:css, "small.error").displayed?
    @driver.find_element(:id, "url").clear
    @driver.find_element(:id, "url").send_keys "http://www.cdlib.org"
    Selenium::WebDriver::Support::Select.new(@driver.find_element(:id, "customDropdown1")).select_by(:text, "Green Chilies")
    @driver.find_element(:id, "password").clear
    @driver.find_element(:id, "password").send_keys "12345678A%"
    @driver.find_element(:id, "confirmPassword").clear
    @driver.find_element(:id, "confirmPassword").send_keys "12345678A%"
    @driver.find_element(:xpath, "//button[@type='submit']").click
    @driver.find_element(:id, "radio2").click
    @driver.find_element(:id, "checkbox1").click
    @driver.find_element(:xpath, "//button[@type='submit']").click
  end
  
  def element_present?(how, what)
    @driver.find_element(how, what)
    true
  rescue Selenium::WebDriver::Error::NoSuchElementError
    false
  end
  
  def alert_present?()
    @driver.switch_to.alert
    true
  rescue Selenium::WebDriver::Error::NoAlertPresentError
    false
  end
  
  def verify(&blk)
    yield
  rescue Test::Unit::AssertionFailedError => ex
    @verification_errors << ex
  end
  
  def close_alert_and_get_its_text(how, what)
    alert = @driver.switch_to().alert()
    alert_text = alert.text
    if (@accept_next_alert) then
      alert.accept()
    else
      alert.dismiss()
    end
    alert_text
  ensure
    @accept_next_alert = true
  end
end
