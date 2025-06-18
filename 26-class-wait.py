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
        self.wait = WebDriverWait(self.driver,wait_in_sec)
        # self.wait = self.driver.implicitly_wait(10)
        self.driver.maximize_window()
    

    def text_textbox_submission(self):
        try:

            self.driver.get("https://demoqa.com/text-box")
            # TODO later
            self._fill_form("Jiten","JitenP@Outlook.Com","PRRA 56, Trivandrum","PRRA 56, Trivandrum")

            print("form filled -->")
            # submit the form 

            submit_button =  self.driver.find_element(By.ID,"submit")

            self.driver.execute_script("arguments[0].scrollIntoView();",submit_button)

            submit_button.click()

            output = self.__get_output()
            assert output["name"]=="Name:Jiten","Name filed mismatch"
            assert output["email"]=="Email:JitenP@Outlook.Com","Email filed mismatch"
            assert output["currentAddress"]=="Current Address :PRRA 56, Trivandrum","Current Address filed mismatch"
            assert output["permanentAddress"]=="Permananet Address :PRRA 56, Trivandrum","Permananet Address filed mismatch"
            print("Form Submission has bee Passed")

        except Exception as e:
            print(f"{str(e)}")
    
    def empty_textbox_submission(self):
        self.driver.get("https://demoqa.com/text-box")
        submit_button =  self.driver.find_element(By.ID,"submit")
        self.driver.execute_script("arguments[0].scrollIntoView();",submit_button)
        submit_button.click()
        output = self.__get_output()
        assert len(output)==0,"Output appeared for the emoty form"
        print("Empty Submission has bee Passed")


    def _fill_form(self,userName,userEmail,currentAddress,permanentAddress):

        self.driver.find_element(By.ID,"userName").send_keys(userName)
        self.driver.find_element(By.ID,"userEmail").send_keys(userEmail)
        self.driver.find_element(By.ID,"currentAddress").send_keys(currentAddress)
        self.driver.find_element(By.ID,"permanentAddress").send_keys(permanentAddress)
        # currentAddress
        # permanentAddress
    
    def __get_output(self):
       output={}
       try:
       # output_element =  self.driver.find_element(By.ID,"output")
        output_element= self.wait.until(EC.visibility_of_element_located((By.ID,"output")))

        output["name"]= output_element.find_element(By.ID,"name").text
        output["email"]= output_element.find_element(By.ID,"email").text
        output["currentAddress"]= output_element.find_element(By.ID,"currentAddress").text
        output["permanentAddress"]= output_element.find_element(By.ID,"permanentAddress").text
        return output
       except Exception as E:
           print(f"{str(E)}")
           return output
         

if __name__=="__main__":
    qa = qaTextBodDemo(10)
    #qa.empty_textbox_submission()
    #time.sleep(2)
    qa.text_textbox_submission()
    time.sleep(2)

# please do this on w3schools -> signup