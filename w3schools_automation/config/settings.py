class Settings:
    # URLs
    BASE_URL = "https://www.w3schools.com"
    LOGIN_URL = f"{BASE_URL}/login"
    
    # Credentials (in real project, use environment variables)
    VALID_EMAIL = "test@example.com"
    VALID_PASSWORD = "securepassword123"
    INVALID_EMAIL = "invalid@example.com"
    INVALID_PASSWORD = "wrongpassword"
    
    # Browser settings
    HEADLESS = True
    BROWSER = "chrome"  # chrome/firefox
    IMPLICIT_WAIT = 10
    EXPLICIT_WAIT = 15
    
    # Paths
    SCREENSHOT_DIR = "screenshots"
    REPORT_DIR = "reports"
    LOG_DIR = "logs"