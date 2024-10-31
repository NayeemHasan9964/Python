from selenium import webdriver

import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

#To handle alerts
driver.find_element(By.CSS_SELECTOR, "input[name = 'enter-name']").send_keys("Alex")
driver.find_element(By.ID, "alertbtn").click()

#Now Switching to alert
alert = driver.switch_to.alert
alertText = alert.text
alert.accept()
print(alertText)





time.sleep(5)