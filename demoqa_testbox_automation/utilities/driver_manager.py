from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from config.config import Config

class DriverManager:
    @staticmethod
    def get_driver():
        """Initialize and return a configured WebDriver instance"""
        chrome_options = Options()
        
        if Config.HEADLESS:
            chrome_options.add_argument("--headless=new")
        
        chrome_options.add_argument(f"--window-size={Config.WINDOW_SIZE}")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        # Additional options to make headless more stealthy
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )
        
        # Set implicit wait
        driver.implicitly_wait(Config.IMPLICIT_WAIT)
        
        return driver