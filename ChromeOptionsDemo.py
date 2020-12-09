from selenium import webdriver
import pytest
import time

#This code is added by Architect in devlop branch

chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("--disable-gpu")
chrome_option.add_argument("headless")  # this will invoke the browser in the backend
chrome_option.add_argument("--start-maximized")
chrome_option.add_argument("--ignore-certificate-errors")


driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver", options=chrome_option)
driver.get("https://rahulshettyacademy.com/angularpractice")

print(driver.title)




