from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(4)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.LINK_TEXT,"Shop").click()


driver.maximize_window()
#Extracting product names
products = driver.find_elements(By.CSS_SELECTOR,"div[class = 'card h-100']")

for names in products:
    ProductName = names.find_element(By.CSS_SELECTOR,"div h4 a").text
    if ProductName == "Blackberry":
        names.find_element(By.CSS_SELECTOR, "div button").click()

#After adding to cart doing a checkout
driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()
#After checkout doing another checkout
driver.find_element(By.CSS_SELECTOR,"button[class = 'btn btn-success']").click()

#handling Auto Suggestive drop down
driver.find_element(By.ID,"country").send_keys("ind")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.XPATH,"//div[@class = 'checkbox checkbox-primary']").click()

#Now Clicking on purchase
driver.find_element(By.XPATH,"//input[@type='submit']").click()
Purchased = driver.find_element(By.CLASS_NAME,"alert").text

assert "Success! Thank you!" in Purchased

driver.close()



