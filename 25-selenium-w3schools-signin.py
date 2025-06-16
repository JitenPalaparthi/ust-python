from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService

from webdriver_manager.chrome import ChromeDriverManager

import time;

driver= webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("https://w3schools.com")

    # 1. find the Sign in button 
    # 2. click sign in button 
    # 3. findout email and password input boxes and fill email and password
    # 4. click on Sigh In 
try:
    print("find the Sign in button ")

    time.sleep(2)

    signin_button = driver.find_element(By.XPATH,"//html/body/div[2]/div[1]/div[3]/div/span[1]")
    signin_button.click()
    print("Sign In button clicked")

    time.sleep(2)

    email_fileld = driver.find_element(By.XPATH,"//html/body/div[2]/div[1]/div[3]/div[2]/div/form/div[1]/input")
    email_fileld.send_keys("jitenp@outlook.com")

    password_field = driver.find_element(By.XPATH,"//html/body/div[2]/div[1]/div[3]/div[2]/div/form/div[2]/div/input")
    password_field.send_keys("jiten123")

    button = driver.find_element(By.XPATH,"//html/body/div[2]/div[1]/div[3]/div[2]/div/form/button")

    button.click()

    time.sleep(10)

    login_status= driver.find_element(By.ID,"loginStatus")
    print(login_status.text)
    if login_status.text == "Invalid username or password":
        print("Test passed")
    else:
        print("Test Failed")

except Exception as e:
    print(f"{str(e)}")

finally:
    time.sleep(2)
    driver.quit()