import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.options import Options

# chrome_option = Options()
# chrome_option.add_argument("--incognito")
driver = webdriver.Chrome()
#switchingTab = ["https://www.google.com","https://www.linkedin.com/feed/","https://www.amazon.com/"]
driver.maximize_window()

# for i in switchingTab:
#     driver.switch_to.new_window("tab")
#     driver.get(i)
#     time.sleep(3)
#     driver.close()

driver.get("https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2F")
driver.find_element(By.ID,"username").send_keys("snayeem341@gmail.com")
driver.find_element(By.ID,"password").send_keys("Sonuzz@9964")
# driver.find_element(By.XPATH,"//input[@name = 'rememberMeOptIn']").click()
driver.find_element(By.CSS_SELECTOR, "button[aria-label='Sign in']").click()




time.sleep(3)