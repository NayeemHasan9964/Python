from itertools import count

from selenium import webdriver

import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()

#To select an item from the dropdown
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(5)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class = 'ui-menu-item'] a")
print(len(countries))
for country in countries:
    if country == "India":
        country.click()
        break
