class Config:
    BASE_URL = "https://demoqa.com"
    TEXT_BOX_URL = f"{BASE_URL}/text-box"
    
    # Headless browser settings
    HEADLESS = True
    WINDOW_SIZE = "1920,1080"
    
    # Timeouts
    IMPLICIT_WAIT = 10
    EXPLICIT_WAIT = 15
    
    # Screenshot settings
    SCREENSHOT_DIR = "screenshots"
    REPORT_DIR = "reports"