import unittest
import logging
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utilities.driver_manager import DriverManager
from pages.login_page import LoginPage
from config.settings import Settings

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f"{Settings.LOG_DIR}/test_log.log"),
        logging.StreamHandler()
    ]
)

class TestW3SchoolsLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = DriverManager.get_driver()
        cls.logger = logging.getLogger(__name__)
        
    def setUp(self):
        self.login_page = LoginPage(self.driver)
        self.logger.info("\n" + "="*50 + f"\nStarting test: {self._testMethodName}\n" + "="*50)
    
    def test_successful_login(self):
        """Test successful login with valid credentials"""
        # Perform login
        self.login_page.login(Settings.VALID_EMAIL, Settings.VALID_PASSWORD)
        
        # Take screenshot
        screenshot_path = self.login_page.take_screenshot(
            f"successful_login_{time.strftime('%Y%m%d_%H%M%S')}.png"
        )
        self.logger.info(f"Screenshot saved to: {screenshot_path}")
        
        # Verify login status
        self.assertTrue(self.login_page.is_login_successful())
        
    def test_invalid_login(self):
        """Test login with invalid credentials"""
        # Perform login with invalid credentials
        self.login_page.login(Settings.INVALID_EMAIL, Settings.INVALID_PASSWORD)
        
        # Take screenshot
        screenshot_path = self.login_page.take_screenshot(
            f"failed_login_{time.strftime('%Y%m%d_%H%M%S')}.png"
        )
        self.logger.info(f"Screenshot saved to: {screenshot_path}")
        
        # Verify error message
        status_text = self.login_page.get_login_status()
        self.assertIn("incorrect", status_text.lower())
        
    def test_password_visibility_toggle(self):
        """Test password visibility toggle functionality"""
        # Enter password (should be hidden by default)
        self.login_page.enter_password(Settings.VALID_PASSWORD)
        self.assertFalse(self.login_page.is_password_visible())
        
        # Toggle visibility
        self.login_page.toggle_password_visibility()
        self.assertTrue(self.login_page.is_password_visible())
        
        # Toggle back
        self.login_page.toggle_password_visibility()
        self.assertFalse(self.login_page.is_password_visible())
        
    def test_capslock_indicator(self):
        """Test Caps Lock indicator functionality"""
        # Verify indicator is hidden initially
        self.assertFalse(self.login_page.is_capslock_indicator_visible())
        
        # Simulate Caps Lock on
        self.login_page.simulate_capslock_on()
        
        # Verify indicator is now visible
        self.assertTrue(self.login_page.is_capslock_indicator_visible())
        
    def test_empty_form_submission(self):
        """Test form submission with empty fields"""
        # Submit empty form
        self.login_page.submit_login()
        
        # Verify error messages for required fields
        email_validation = self.login_page.driver.execute_script(
            "return document.getElementById('tnb-login-dropdown-email').validationMessage"
        )
        self.assertEqual(email_validation, "Please fill out this field.")
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        cls.logger.info("Test suite completed")

if __name__ == "__main__":
    unittest.main()