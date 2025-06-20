import time
import warnings

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

class modal:

    def __init__(self,wait_in_sec=30):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.wait = WebDriverWait(driver=self.driver,timeout=wait_in_sec)
        self.driver.maximize_window()

    def find_modal(self): 
        self.driver.get("https://demoqa.com/modal-dialogs")
        showSmallModal_button=self.driver.find_element(By.ID,"showSmallModal")
        self.driver.execute_script("arguments[0].scrollIntoView();",showSmallModal_button)
        # execute_script is to execute java script 
        showSmallModal_button.click()

if __name__== "__main__":
    d1=modal(10)
    d1.find_modal()
    time.sleep(5)
    d1.driver.quit()