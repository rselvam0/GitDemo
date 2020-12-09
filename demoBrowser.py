from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path= "C:\Drivers\chromedriver")
#driver.get("http://demo.automationtesting.in/Windows.html")
driver.get("http://rahulshettyacademy.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

driver.get("http://rahulshettyacademy.com/AutomationPractice/")
driver.minimize_window()
driver.back()

driver.refresh()

driver.close()
