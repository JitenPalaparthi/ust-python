import time
import warnings

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC


class qaTextBodDemo:

    def __init__(self,wait_in_sec=30):
        # initialize the driver, probably chrome
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver,wait_in_sec,timeout=30,poll_frequency=5)
        # self.wait = self.driver.implicitly_wait(10)
        self.driver.maximize_window()
    

    def text_textbox_submission(self):
        self.driver.get("https://demoqa.com/text-box")
        # TODO later
        self._fill_form("Jiten","JitenP@Outlook.Com","PRRA 56, Trivandrum","PRRA 56 Trivandrum")

        print("form filled -->")
        # submit the form 

        submit_button =  self.driver.find_element(By.ID,"submit")

        self.driver.execute_script("arguments[0].scrollIntoView();",submit_button)

        submit_button.click()
    
    def emoty_textbox_submission(self):
        self.driver.get("https://demoqa.com/text-box")
        submit_button =  self.driver.find_element(By.ID,"submit")
        self.driver.execute_script("arguments[0].scrollIntoView();",submit_button)
        submit_button.click()


    def _fill_form(self,userName,userEmail,currentAddress,permanentAddress):

        self.driver.find_element(By.ID,"userName").send_keys(userName)
        self.driver.find_element(By.ID,"userEmail").send_keys(userEmail)
        self.driver.find_element(By.ID,"currentAddress").send_keys(currentAddress)
        self.driver.find_element(By.ID,"permanentAddress").send_keys(permanentAddress)
        # currentAddress
        # permanentAddress
    

if __name__=="__main__":
    qa = qaTextBodDemo(10)
    qa.emoty_textbox_submission()
    time.sleep(10)
    qa.text_textbox_submission()
    time.sleep(10)

# please do this on w3schools -> signup