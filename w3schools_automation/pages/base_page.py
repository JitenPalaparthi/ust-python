from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
import os
import logging
from config.settings import Settings

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Settings.EXPLICIT_WAIT)
        self.logger = logging.getLogger(__name__)
    
    def click(self, locator, timeout=None):
        """Click on an element after ensuring it's clickable"""
        wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        try:
            element = wait.until(EC.element_to_be_clickable(locator))
            element.click()
            self.logger.info(f"Clicked on element: {locator}")
        except TimeoutException:
            self.logger.error(f"Element not clickable: {locator}")
            raise
    
    def enter_text(self, locator, text, clear=True):
        """Enter text into a field after ensuring it's visible"""
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            if clear:
                element.clear()
            element.send_keys(text)
            self.logger.info(f"Entered text '{text}' in element: {locator}")
        except TimeoutException:
            self.logger.error(f"Element not visible for text entry: {locator}")
            raise
    
    def get_text(self, locator):
        """Get text from an element"""
        try:
            text = self.wait.until(EC.visibility_of_element_located(locator)).text
            self.logger.info(f"Got text '{text}' from element: {locator}")
            return text
        except TimeoutException:
            self.logger.error(f"Element not visible for getting text: {locator}")
            raise
    
    def is_visible(self, locator, timeout=None):
        """Check if element is visible"""
        wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        try:
            return bool(wait.until(EC.visibility_of_element_located(locator)))
        except TimeoutException:
            return False
    
    def take_screenshot(self, filename):
        """Take screenshot and save to screenshots directory"""
        if not os.path.exists(Settings.SCREENSHOT_DIR):
            os.makedirs(Settings.SCREENSHOT_DIR)
        path = os.path.join(Settings.SCREENSHOT_DIR, filename)
        try:
            self.driver.save_screenshot(path)
            self.logger.info(f"Screenshot saved to: {path}")
            return path
        except WebDriverException as e:
            self.logger.error(f"Failed to take screenshot: {e}")
            raise
    
    def scroll_to_element(self, locator):
        """Scroll to make element visible"""
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
            self.logger.info(f"Scrolled to element: {locator}")
            return element
        except TimeoutException:
            self.logger.error(f"Element not present for scrolling: {locator}")
            raise