from selenium import webdriver
import pytest
import time

#This code added by Architect in develop branch

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver")
driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element_by_link_text("Click Here").click()
childWindow = driver.window_handles[0]
parentWindow = driver.window_handles[1]

driver.switch_to.window(childWindow)
print(driver.find_element_by_tag_name("h3").text)

driver.switch_to.window(parentWindow)
print(driver.find_element_by_tag_name("h3").text)
