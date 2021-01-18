from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Open the web browser
driver = webdriver.Chrome()
driver.get("http://www.instagram.com")
assert "Instagram" in driver.title

# Log in (sleep to load the pages)
time.sleep(4)
username = driver.find_element_by_xpath("//input[@name='username']")
username.send_keys("salad.robot")
time.sleep(.1231)
password = driver.find_element_by_xpath("//input[@name='password']")
password.send_keys("travisscott")
time.sleep(3)
login = driver.find_element_by_xpath("//button[contains(.,'Log In')]")
login.click()

