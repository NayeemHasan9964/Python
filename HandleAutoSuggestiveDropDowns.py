from selenium import webdriver

import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()

#To select an item from the Auto Suggestive dropdown
driver.find_element(By.ID, "autosuggest").send_keys("ind")  
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class = 'ui-menu-item'] a")
print(len(countries))
for country in countries:
    if country.text == "India":
        country.click()
        break
assert  driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"
time.sleep(5)