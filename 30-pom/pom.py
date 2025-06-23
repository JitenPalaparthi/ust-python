import time
import warnings
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



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

    SUCCESS_MODEL_ID = EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg"))

    SUBMITTED_DATA_XPATH = EC.visibility_of_any_elements_located((By.XPATH, "//table//td[2]"))#driver.find_elements(By.XPATH, "//table//td[2]")

    def __init__(self,wait_in_seconds=10):
          super().__init__(wait_in_seconds)
        

    def submit_form(self):
        try:
            self.driver.get(PracticeForm.URL)

            WebDriverWait(self.driver, 1).until(PracticeForm.FIRST_NAME_ID).send_keys("John")
            WebDriverWait(self.driver, 1).until(PracticeForm.LAST_NAME_ID).send_keys("Doe")
            WebDriverWait(self.driver, 1).until(PracticeForm.EMAIL_ID).send_keys("john.doe@example.com")
        
            gender_male = WebDriverWait(self.driver, 1).until(PracticeForm.GENDER_ID)
            self.driver.execute_script("arguments[0].click();", gender_male)
            WebDriverWait(self.driver, 1).until(PracticeForm.USER_NUMBER_ID).send_keys("1234567890")
            
            dob= WebDriverWait(self.driver, 1).until(PracticeForm.DATE_OF_BIRTH_ID)
            dob.send_keys("")
            dob.send_keys("Jun 2025"+Keys.RETURN)

            subjects_input = WebDriverWait(self.driver, 10).until(
            PracticeForm.SUBJECTS_INPUT_ID).send_keys("Comp")

            WebDriverWait(self.driver, 5).until(
            PracticeForm.SUBJECT_CONTAINS_XPATH).click()

            hobbies_sports = WebDriverWait(self.driver, 1).until(PracticeForm.HOBBIES_XPATH)
            self.driver.execute_script("arguments[0].click();", hobbies_sports)
            
            WebDriverWait(self.driver, 5).until(
            PracticeForm.UPLOAD_PIC_ID).send_keys(PracticeForm.PIC_PATH)

            WebDriverWait(self.driver, 5).until(
            PracticeForm.CURRENT_ADDRESS_ID).send_keys("123 Main Street, Apt 4B, New York, NY 10001")

            state =  WebDriverWait(self.driver, 5).until(
            PracticeForm.STATE_ID)
            self.driver.execute_script("arguments[0].scrollIntoView();", state)
            state.click()

            WebDriverWait(self.driver, 5).until(
            PracticeForm.STATE_OPTION_XPATH).click()


            city =  WebDriverWait(self.driver, 5).until(
            PracticeForm.CITY_ID)
            self.driver.execute_script("arguments[0].scrollIntoView();", city)
            city.click()

            WebDriverWait(self.driver, 5).until(
            PracticeForm.CITY_OPTION_XPATH).click()

            WebDriverWait(self.driver, 5).until(
            PracticeForm.SUBMIT_ID).click()
        except Exception as e:
            print(f"{str(e)}")

    def validate_form(self):
        try:
            success_modal =  WebDriverWait(self.driver, 10).until(
            PracticeForm.SUCCESS_MODEL_ID)
            print("Form submitted successfully!")
            
            # Print submitted data
            submitted_data= WebDriverWait(self.driver, 10).until(
            PracticeForm.SUBMITTED_DATA_XPATH)
            
            print("\nSubmitted Data:")
            for data in submitted_data:
                print(data.text)
        
        except Exception as e:
            print(f"Form submission failed: {str(e)}")


if __name__=="__main__":
   
   pf= PracticeForm(10)
   pf.submit_form()
   time.sleep(2)
   pf.validate_form()
   time.sleep(5)
   pf.driver.quit()

        

    
