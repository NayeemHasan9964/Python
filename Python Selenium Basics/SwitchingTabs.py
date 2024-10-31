import time

from selenium import webdriver

driver = webdriver.Chrome()
switchingTab = ["https://www.google.com","https://www.linkedin.com/feed/","https://www.amazon.com/"]
driver.maximize_window()

for i in switchingTab:
    driver.switch_to.new_window("tab")
    driver.get(i)
    time.sleep(3)
    driver.close()