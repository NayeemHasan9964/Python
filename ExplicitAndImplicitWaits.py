from selenium import webdriver

import time

from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.implicitly_wait(5)
expectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actualList = [ ]
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH,"//div[@class='products']/div")
count = len(results)
assert count > 0
for text in results:
    rl = text.find_element(By.CSS_SELECTOR,"div h4").text
    actualList.append(rl)
print(actualList)
assert expectedList == actualList
for result in results:
    result.find_element(By.XPATH, "div/button").click()
driver.find_element(By.CSS_SELECTOR,"img[alt = 'Cart']").click()
driver.find_element(By.CSS_SELECTOR,"div[class='cart-preview active'] button").click()

#After proceeding to the cart and validating the Sum
CartValue = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for price in CartValue:
    sum = sum + int(price.text)
print(sum)
TotalAMount = int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
assert  sum == TotalAMount

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH, "//button[text() = 'Apply']").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,'.promoInfo')))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)
#Assignment1
discountAmount = float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)
assert discountAmount < TotalAMount

#To place Order
driver.find_element(By.XPATH,"//button[text() = 'Place Order' ]").click()
wait = WebDriverWait(driver, 10)
driver.find_element(By.CSS_SELECTOR,"div[class = 'wrapperTwo'] select").send_keys("India")
wait = WebDriverWait(driver, 10)
