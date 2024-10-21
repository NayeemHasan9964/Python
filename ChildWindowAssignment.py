from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"Free Access to InterviewQues/ResumeAssistance/Material").click()

#Moving to ChildWindow and extracting the Text
windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])
textExtraction = driver.find_element(By.CSS_SELECTOR,".im-para.red").text
StringList = textExtraction.split(' ')
print(StringList)
emailID = (StringList[4])
driver.close()

#Now Moving back to Parent Window
driver.switch_to.window(windowsOpened[0])
driver.find_element(By.ID,"username").send_keys(emailID)
driver.find_element(By.ID,"password").send_keys(12345)
driver.find_element(By.CSS_SELECTOR,"input[value = 'admin']").click()
dropDown = Select(driver.find_element(By.CSS_SELECTOR,".form-control[data-style='btn-info']"))
dropDown.select_by_index(0)
driver.find_element(By.CSS_SELECTOR,"input[name = 'terms']").click()
driver.find_element(By.CSS_SELECTOR,"input[name = 'signin']").click()
wait = WebDriverWait(driver,20)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR,".alert-danger").text)











