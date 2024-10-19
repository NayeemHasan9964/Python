from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

#Locators = ID, ClassName,linkText,CSSSelector,name,Xpath
driver.find_element(By.NAME, "email").send_keys("alexmercer@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("12345678")
driver.find_element(By.ID ,"exampleCheck1").click()

#To create Xpath -> //Tagname[@attribute = 'value'] ->//input[@type='submit']
driver.find_element(By.XPATH, "//input[@type='submit']").click()

#Static DropDown
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_index(0)

#To Create CSS Selector ->tagname[attribute = 'value']
driver.find_element(By.CSS_SELECTOR, "input[name= 'name']").send_keys("AlexMercer")
message = driver.find_element(By.CLASS_NAME,"alert-success").text
driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()
assert "Success" in message
print(message)
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("AlexMerxer")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()
time.sleep(5)
