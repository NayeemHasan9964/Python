from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client")
driver.maximize_window()
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("alex@gmail.com")
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys("123456")
driver.find_element(By.ID, "confirmPassword").send_keys("123456")
# driver.find_element(By.XPATH, "//button[@type='submit']").click()
driver.find_element(By.XPATH,"//button[text()='Save New Password']").click()






time.sleep(5)