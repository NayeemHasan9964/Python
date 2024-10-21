import time

from selenium import webdriver

#To Handle Chrome in Desired State
ChromeOptions = webdriver.ChromeOptions()
ChromeOptions.add_argument("headless")
ChromeOptions.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(options=ChromeOptions)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# driver.get_screenshot_as_file("Screen.png")

