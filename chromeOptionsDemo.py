from selenium import webdriver
from selenium.webdriver.common.by import By

#To invoke Chrome in our Desired State we can use
Chrome_Options = webdriver.ChromeOptions()
Chrome_Options.add_argument("--start-maximized")
Chrome_Options.add_argument("headless")
Chrome_Options.add_argument("--ignore-certificate-errors")


driver = webdriver.Chrome(options=Chrome_Options)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
print(driver.title)