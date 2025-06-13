# pip3 install selenium 
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
#driver = webdriver.Chrome()

service = Service("/Users/jiten/Downloads/chromedriver-mac-arm64/chromedriver")
driver= webdriver.Chrome(service=service)
driver.get("https://www.w3schools.com")
print(driver.title)
time.sleep(10)
driver.quit()