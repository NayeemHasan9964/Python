import time
from selenium import webdriver

# List of URLs to visit
switchingTab = ["https://www.google.com", "https://www.linkedin.com/feed/", "https://www.amazon.com/"]

# Initialize the browser
driver = webdriver.Chrome()

try:
    driver.maximize_window()

    for i in switchingTab:
        # Open a new tab
        driver.switch_to.new_window('tab')

        # Navigate to the URL
        driver.get(i)

        # Pause to allow the page to load
        time.sleep(3)

    # Add additional logic here if needed

finally:
    # Quit the browser after all actions
    driver.quit()


