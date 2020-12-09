from selenium import webdriver
import pytest
import time

# this code is added by Architect in develop branch

driver = webdriver.Chrome(executable_path= "C:\Drivers\chromedriver")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element_by_css_selector("input#name").send_keys("option3")
driver.find_element_by_id("alertbtn").click()

alert = driver.switch_to.alert
assert "option3" in alert.text
alert.accept()  # to click on ok button on alert.
# alert.dismiss() # to click cancel button on alert.

