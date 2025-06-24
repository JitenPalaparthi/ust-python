from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from config.settings import Settings
import time

class LoginPage(BasePage):
    # Locators
    LOGIN_FORM = (By.ID, "loginFormElement")
    EMAIL_FIELD = (By.ID, "tnb-login-dropdown-email")
    PASSWORD_FIELD = (By.ID, "tnb-login-dropdown-password")
    TOGGLE_PASSWORD = (By.ID, "toggle-password-visibility")
    CAPSLOCK_INDICATOR = (By.ID, "capslock-indicator")
    FORGOT_PASSWORD = (By.ID, "tnb-login-dropdown-reset-password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "#loginFormElement button[type='submit']")
    LOGIN_STATUS = (By.ID, "loginStatus")
    LOADER = (By.CLASS_NAME, "button-loader")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Settings.LOGIN_URL)
        self.wait.until(EC.presence_of_element_located(self.LOGIN_FORM))
    
    def enter_email(self, email):
        self.enter_text(self.EMAIL_FIELD, email)
        return self
    
    def enter_password(self, password):
        self.enter_text(self.PASSWORD_FIELD, password)
        return self
    
    def toggle_password_visibility(self):
        self.click(self.TOGGLE_PASSWORD)
        return self
    
    def is_password_visible(self):
        return self.PASSWORD_FIELD.get_attribute("type") == "text"
    
    def is_capslock_indicator_visible(self):
        return self.is_visible(self.CAPSLOCK_INDICATOR)
    
    def click_forgot_password(self):
        self.click(self.FORGOT_PASSWORD)
        # Return whatever page comes next
        return self
    
    def submit_login(self):
        self.click(self.SUBMIT_BUTTON)
        # Wait for loader to disappear
        self.wait.until(EC.invisibility_of_element_located(self.LOADER))
        return self
    
    def get_login_status(self):
        return self.get_text(self.LOGIN_STATUS)
    
    def is_login_successful(self):
        return "success" in self.get_login_status().lower()
    
    def login(self, email, password):
        """Complete login flow"""
        (self.enter_email(email)
         .enter_password(password)
         .submit_login())
        return self
    
    def simulate_capslock_on(self):
        """Simulate Caps Lock being on (for testing the indicator)"""
        self.driver.execute_script("""
            const event = new KeyboardEvent('keydown', {
                key: 'CapsLock',
                keyCode: 20,
                which: 20,
                shiftKey: false,
                getModifierState: (key) => key === 'CapsLock' ? true : false
            });
            document.dispatchEvent(event);
        """)
        time.sleep(1)  # Allow UI to update
        return self