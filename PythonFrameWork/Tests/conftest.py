import pytest
from selenium import webdriver



@pytest.fixture(scope= 'class')
def browserSetup(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(4)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver =driver
    yield
    driver.close()
