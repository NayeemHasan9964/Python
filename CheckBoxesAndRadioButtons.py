from selenium import webdriver

import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.ID,"autocomplete").send_keys("ind")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] div")
print(len(countries))
for country in countries:
    if country.text == "India":
        country.click()  # Click the option when found
        break
print(driver.find_element(By.ID,"autocomplete").get_attribute("value"))

time.sleep(5)