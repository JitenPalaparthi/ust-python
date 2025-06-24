import unittest
import time
from utilities.driver_manager import DriverManager
from pages.text_box_page import TextBoxPage
from config.config import Config

class TestTextBox(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = DriverManager.get_driver()
        
    def setUp(self):
        self.text_box_page = TextBoxPage(self.driver)
        self.test_data = {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "current_address": "123 Main St, Apt 4B\nNew York, NY 10001",
            "permanent_address": "456 Oak Ave\nLos Angeles, CA 90001"
        }
    
    def test_successful_form_submission(self):
        """Test happy path form submission"""
        # Fill and submit form
        self.text_box_page.fill_and_submit_form(
            self.test_data["name"],
            self.test_data["email"],
            self.test_data["current_address"],
            self.test_data["permanent_address"]
        )
        
        # Take screenshot
        screenshot_path = self.text_box_page.take_screenshot(
            f"successful_submission_{time.strftime('%Y%m%d_%H%M%S')}.png"
        )
        print(f"Screenshot saved to: {screenshot_path}")
        
        # Verify output is visible
       # self.assertTrue(self.text_box_page.is_output_visible())
        
        # Verify output values
        self.assertEqual(self.text_box_page.get_output_name(), self.test_data["name"])
        self.assertEqual(self.text_box_page.get_output_email(), self.test_data["email"])
        self.assertEqual(
            self.text_box_page.get_output_current_address(),
            self.test_data["current_address"].replace("\n", " ")
        )
        print( "------->>>>>>>>",self.text_box_page.get_output_permanent_address())

        self.assertEqual(
            self.text_box_page.get_output_permanent_address(),"Permananet Address :456 Oak Ave Los Angeles, CA 90001"
        )
    
    def test_empty_form_submission(self):
        """Test form submission with no data"""
        # Submit empty form
        self.text_box_page.submit_form()
        
        # Verify no output is shown
        #self.assertFalse(self.text_box_page.is_output_visible())
        
        # Take screenshot
        screenshot_path = self.text_box_page.take_screenshot(
            f"empty_submission_{time.strftime('%Y%m%d_%H%M%S')}.png"
        )
        print(f"Screenshot saved to: {screenshot_path}")
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()