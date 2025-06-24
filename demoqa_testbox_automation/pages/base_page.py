from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
from config.config import Config

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.EXPLICIT_WAIT)
    
    def click(self, locator):
        """Click on an element after ensuring it's clickable"""
        self.wait.until(EC.element_to_be_clickable(locator)).click()
    
    def enter_text(self, locator, text):
        """Enter text into a field after ensuring it's visible"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        """Get text from an element"""
        return self.wait.until(EC.visibility_of_element_located(locator)).text
    
    def is_visible(self, locator):
        """Check if element is visible"""
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            return False
    
    def take_screenshot(self, filename):
        """Take screenshot and save to screenshots directory"""
        if not os.path.exists(Config.SCREENSHOT_DIR):
            os.makedirs(Config.SCREENSHOT_DIR)
        path = os.path.join(Config.SCREENSHOT_DIR, filename)
        self.driver.save_screenshot(path)
        return path
    
    def scroll_to_element(self, locator):
        """Scroll to make element visible"""
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return element