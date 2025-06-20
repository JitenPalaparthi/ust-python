# alertButton
import time
import warnings

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

WebDriverWait(driver,10)

driver.maximize_window()
driver.get("https://demoqa.com/alerts")

alert_button=WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID,"alertButton")))
#alert_button= driver.find_element(By.ID,"alertButton")

alert_button.click()


if WebDriverWait(driver, 5).until(EC.alert_is_present()):

    assert driver.switch_to.alert.text=="You clicked a button","Alert test is failed"
    print("Alert test is Passed")
    print("alert is present")
    time.sleep(3)
    driver.switch_to.alert.accept()

    # if "You clicked a button" == driver.switch_to.alert.text:
    #     print("Alert test is Passed")
    #     print("alert is present")
    #     time.sleep(3)
    #     driver.switch_to.alert.accept()
    # else:
    #     print("Alert test is failed")
#timerAlertButton

timerAlertButton=WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID,"timerAlertButton")))

#timerAlertButton= driver.find_element(By.ID,"timerAlertButton")

timerAlertButton.click()

if WebDriverWait(driver, 6).until(EC.alert_is_present()):

    assert driver.switch_to.alert.text=="This alert appeared after 5 seconds","Alert test is failed"
    print("Await Alert test is Passed")
    print("alert is present")
    time.sleep(1)
    driver.switch_to.alert.accept()

    

