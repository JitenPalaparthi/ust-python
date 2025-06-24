from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.config import Config

class TextBoxPage(BasePage):
    # Input field locators
    FULL_NAME = (By.ID, "userName")
    EMAIL = (By.ID, "userEmail")
    CURRENT_ADDRESS = (By.ID, "currentAddress")
    PERMANENT_ADDRESS = (By.ID, "permanentAddress")
    SUBMIT_BUTTON = (By.ID, "submit")
    
    # Output field locators
    OUTPUT_DIV = (By.ID, "output")
    OUTPUT_NAME = (By.ID, "name")
    OUTPUT_EMAIL = (By.ID, "email")
    OUTPUT_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    OUTPUT_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Config.TEXT_BOX_URL)
    
    def enter_full_name(self, name):
        self.enter_text(self.FULL_NAME, name)
        return self  # For method chaining
    
    def enter_email(self, email):
        self.enter_text(self.EMAIL, email)
        return self
    
    def enter_current_address(self, address):
        self.enter_text(self.CURRENT_ADDRESS, address)
        return self
    
    def enter_permanent_address(self, address):
        self.enter_text(self.PERMANENT_ADDRESS, address)
        return self
    
    def submit_form(self):
        self.scroll_to_element(self.SUBMIT_BUTTON)
        self.click(self.SUBMIT_BUTTON)
        return self
    
    def is_output_visible(self):
        return self.is_visible(self.OUTPUT_DIV)
    
    def get_output_name(self):
        return self._clean_output_text(self.get_text(self.OUTPUT_NAME), "Name:")
    
    def get_output_email(self):
        return self._clean_output_text(self.get_text(self.OUTPUT_EMAIL), "Email:")
    
    def get_output_current_address(self):
        return self._clean_output_text(
            self.get_text(self.OUTPUT_CURRENT_ADDRESS), 
            "Current Address :"
        )
    
    def get_output_permanent_address(self):
        return self._clean_output_text(
            self.get_text(self.OUTPUT_PERMANENT_ADDRESS), 
            "Permanent Address :"
        )
    
    def _clean_output_text(self, text, prefix):
        """Helper method to clean output text"""
        return text.replace(prefix, "").strip()
    
    def fill_and_submit_form(self, name, email, current_address, permanent_address):
        """Complete form submission flow"""
        (self.enter_full_name(name)
         .enter_email(email)
         .enter_current_address(current_address)
         .enter_permanent_address(permanent_address)
         .submit_form())
        return self