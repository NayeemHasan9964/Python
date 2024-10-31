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
assert driver.find_element(By.ID,"autocomplete").get_attribute("value") == "India"

#To fill CheckBoxes
checkboxes = driver.find_elements(By.XPATH, "//input[@type = 'checkbox']")
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
# To check Radia Buttons
radioButtons = driver.find_elements(By.CSS_SELECTOR, "input[type = 'radio']")
for radioButton in radioButtons:
    if radioButton.get_attribute("value") == "radio1":
        radioButton.click()
        assert radioButton.is_selected()

time.sleep(5)