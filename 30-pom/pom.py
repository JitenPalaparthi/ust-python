import time
import warnings
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseClass:

       def __init__(self,wait_in_sec=10):
        # initialize the driver, probably chrome
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver,wait_in_sec)
        # self.wait = self.driver.implicitly_wait(10)
        self.driver.maximize_window()

class PracticeForm(BaseClass):

    URL = "https://demoqa.com/automation-practice-form"
    PIC_PATH= "/Users/jiten/workspace/training/ust-python/pic.png"

    FIRST_NAME_ID =  EC.presence_of_element_located((By.ID, "firstName"))
    LAST_NAME_ID  =  EC.presence_of_element_located((By.ID, "lastName"))#driver.find_element(y.ID, "lastName")
    EMAIL_ID     =  EC.presence_of_element_located((By.ID, "userEmail"))# driver.find_element(By.ID, "userEmail")
    GENDER_ID    =  EC.presence_of_element_located((By.ID, "gender-radio-1"))#driver.find_element(By.ID, "gender-radio-1")
    USER_NUMBER_ID = EC.presence_of_element_located((By.ID, "userNumber"))
   
    DATE_OF_BIRTH_ID = EC.presence_of_element_located((By.ID, "dateOfBirthInput"))
    
    SUBJECTS_INPUT_ID = EC.presence_of_element_located((By.ID, "subjectsInput"))
    SUBJECT_CONTAINS_XPATH=  EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Computer Science')]"))
   
    HOBBIES_XPATH= EC.presence_of_element_located((By.XPATH, '//*[@id="hobbies-checkbox-1"]'))
  
    UPLOAD_PIC_ID= EC.presence_of_element_located((By.ID, "uploadPicture"))
   
    CURRENT_ADDRESS_ID= EC.presence_of_element_located((By.ID, "currentAddress"))
    STATE_ID= EC.presence_of_element_located((By.ID, "state"))
    STATE_OPTION_XPATH=EC.presence_of_element_located((By.XPATH, "//div[text()='NCR']"))
    
    CITY_ID= EC.presence_of_element_located((By.ID, "city"))
    CITY_OPTION_XPATH=EC.presence_of_element_located((By.XPATH, "//div[text()='Delhi']"))

    SUBMIT_ID =  EC.presence_of_element_located((By.ID, "submit"))

    SUCCESS_MODEL_ID=EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg"))

    SUBMITTED_DATA_XPATH= EC.visibility_of_any_elements_located((By.XPATH, "//table//td[2]"))#driver.find_elements(By.XPATH, "//table//td[2]")

    def __init__(self,wait_in_seconds=10):
          super().__init__(wait_in_seconds)
        








if __name__=="__main__":
   pf= PracticeForm(10)
   time.sleep(5)
   pf.driver.quit()

        

    
