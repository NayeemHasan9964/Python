from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"Click Here").click()

windowsOpened = driver.window_handles

#To Switch into new window
driver.switch_to.window(windowsOpened[1])
print(driver.find_element(By.TAG_NAME,"h3").text)
wait = WebDriverWait(driver,10)
wait.until(presence_of_element_located((By.TAG_NAME,"h3")))
driver.close()

#Now switching back to Parent Window
driver.switch_to.window(windowsOpened[0])
print(driver.find_element(By.TAG_NAME,"h3").text)



