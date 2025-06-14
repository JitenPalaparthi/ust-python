from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service as ChromeService

from selenium.webdriver.edge.service import Service as EdgeService

from webdriver_manager.chrome import ChromeDriverManager
# pip install webdriver_manager

from webdriver_manager.microsoft import EdgeChromiumDriverManager

import time

import warnings

warnings.filterwarnings("ignore",category=UserWarning,module="urllib3")

def test_google_search(browser_name):

    """ Testing google.com functionaliy
     This should work with Chrome and also Edge
    """
    try:
        
        if browser_name.lower()=="chrome":
            print("\ntesting with chrome browser")
            # cdm = ChromeDriverManager()
            # cdm.install()
            driver= webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif  browser_name.lower()=="edge":
            print("\ntesting with edge browser")
            driver= webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        else:
            raise ValueError("Supported browsers are chrome or edge")

        driver.implicitly_wait(10)

        driver.get("https://google.com")
        print("Google site is opened")
       
        try:
            accept_button =  driver.find_element(By.XPATH,'//button/div[contains(text(),"Accept all")]')
            accept_button.click()
            print("cookies are acepted")
            time.sleep(1)
        except:
            pass

        try:
            #stay_signed_out= driver.find_element(By.XPATH,"//html/body/div[4]/div/div[2]/div/div/div/div[2]/div/promo-button-text[1]/div/div")
            stay_signed_out=driver.find_element(By.XPATH,'//*[@id="stUuGf"]/div/div[2]/div/div/div/div[2]/div/promo-button-text[1]/div/div')
            stay_signed_out.click()
            print("staying signedout mode")
            time.sleep(1)
        except Exception as e1:
            print(f"somethign went wrong---> {str(e1)}")
            pass
        # //html/body/div[4]/div/div[2]/div/div/div/div[2]/div/promo-button-text[1]/div/div
         # //*[@id="stUuGf"]/div/div[2]/div/div/div/div[2]/div/promo-button-text[1]/div/div
        serch_box= driver.find_element(By.NAME,"q")
        serch_box.send_keys("Selenium Python"+Keys.RETURN) # return is goign to enter automatically
        print("Searching for Selenium Python in Google.Com search box")

        time.sleep(10)

        results = driver.find_elements(By.CSS_SELECTOR,"h3")

        # if len(results)>0:
        #     pass
        # else:
        #     print("No Search Results Found")

        assert len(results)>0, "No Search Results Found"
        print(f"Found {len(results)} upon search")

        assert "Selenium Python" in driver.title

        first_result = results[0]

        first_result.click()

        print("clicked the first result")

        time.sleep(1)

        assert "selenium" in driver.current_url.lower() or "selenium" in driver.title.lower()

        print("\n Test passed")

    except Exception as e:
        print(f"test has Failed {str(e)}")
        # to take a screen shot on failure 
        driver.save_screenshot(f"test_failure_{browser_name}.png")
    
    finally:
        if 'driver' in locals():
            driver.quit()
            print("\n Quit the driver/browser")
            
if __name__ == "__main__": # func main(){}

    browsers=["Chrome"]
    # for browser in ["Chrome","Edge"]:
    for browser in browsers:
        test_google_search(browser)

     











