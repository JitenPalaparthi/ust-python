from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from config.settings import Settings
import logging

class DriverManager:
    @staticmethod
    def get_driver():
        """Initialize and return a configured WebDriver instance"""
        try:
            if Settings.BROWSER.lower() == "chrome":
                return DriverManager._get_chrome_driver()
            elif Settings.BROWSER.lower() == "firefox":
                return DriverManager._get_firefox_driver()
            else:
                raise ValueError(f"Unsupported browser: {Settings.BROWSER}")
        except Exception as e:
            logging.error(f"Failed to initialize WebDriver: {e}")
            raise

    @staticmethod
    def _get_chrome_driver():
        """Configure Chrome WebDriver"""
        chrome_options = ChromeOptions()
        
        if Settings.HEADLESS:
            chrome_options.add_argument("--headless=new")
        
        chrome_options.add_argument(f"--window-size=1920,1080")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        
        # Disable automation flags
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        
        # Additional options for better headless experience
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-infobars")
        
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=chrome_options
        )
        
        # Set implicit wait
        driver.implicitly_wait(Settings.IMPLICIT_WAIT)
        
        return driver

    @staticmethod
    def _get_firefox_driver():
        """Configure Firefox WebDriver"""
        firefox_options = FirefoxOptions()
        
        if Settings.HEADLESS:
            firefox_options.add_argument("--headless")
        
        firefox_options.add_argument("--width=1920")
        firefox_options.add_argument("--height=1080")
        
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=firefox_options
        )
        
        # Set implicit wait
        driver.implicitly_wait(Settings.IMPLICIT_WAIT)
        
        return driver