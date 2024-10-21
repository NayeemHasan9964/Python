#To Practic Go to another site

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()

driver.switch_to.frame("mce_0_ifr")
wait = WebDriverWait(driver,10)
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[aria-label='Close'] svg"))
).click()
driver.find_element(By.ID,"tinymce").clear()
driver.find_element(By.ID,"tinymce").send_keys("Handling Frames")
