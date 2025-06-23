import time
import warnings

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC


class form:
    def __init__(self,wait_in_sec=30):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.wait = WebDriverWait(driver=self.driver,timeout=wait_in_sec)
        self.driver.maximize_window()
    
    def enter_value(self,first_name,last_name):
        self.driver.get("https://demoqa.com/automation-practice-form")
        self.driver.find_element(By.ID, "firstName").send_keys(first_name)
        self.driver.find_element(By.ID, "lastName").send_keys(last_name)


s1=form(10)
s1.enter_value("first","second")
time.sleep(10)
s1.driver.quit()