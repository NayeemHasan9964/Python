from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

BrowserSortedVeggies = []
#Click on Colum Header
driver.find_element(By.XPATH,"//span[text() = 'Veg/fruit name']").click()

#Collect all the names from the list
VeggieWebElements = driver.find_elements(By.XPATH,"//tr/td[1]")
for ele in VeggieWebElements:
    BrowserSortedVeggies.append(ele.text)
print(BrowserSortedVeggies)

OriginalList = BrowserSortedVeggies.copy()
print(OriginalList)

#Sort the Veggies
BrowserSortedVeggies.sort()

#Compare the Two lists
assert BrowserSortedVeggies == OriginalList

