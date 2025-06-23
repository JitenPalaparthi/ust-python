from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# Initialize Chrome WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)

# Open the practice form
driver.get("https://demoqa.com/automation-practice-form")

# Fill in the form
# 1. Name
first_name = wait.until(EC.presence_of_element_located((By.ID, "firstName")))
first_name.send_keys("John")

last_name = driver.find_element(By.ID, "lastName")
last_name.send_keys("Doe")

# 2. Email
email = driver.find_element(By.ID, "userEmail")
email.send_keys("john.doe@example.com")


# 3. Gender (select Male)
gender_male = driver.find_element(By.ID, "gender-radio-1")
driver.execute_script("arguments[0].click();", gender_male)

# gender_male2 = driver.find_element(By.XPATH,'//*[@id="genterWrapper"]/div[2]/div[1]/label')
# gender_male2.click()
# 4. Mobile Number
mobile = driver.find_element(By.ID, "userNumber")
mobile.send_keys("1234567890")


# 5. Date of Birth
dob = driver.find_element(By.ID, "dateOfBirthInput")
dob.send_keys("")
dob.send_keys("Jun 2025"+Keys.RETURN)

# time.sleep(10)
# # Select month
# month_dropdown = driver.find_element(By.CLASS_NAME, "react-datepicker__month-select")
# month_dropdown.send_keys("May")

# # Select year
# year_dropdown = driver.find_element(By.CLASS_NAME, "react-datepicker__year-select")
# year_dropdown.send_keys("1990")

# # Select day
# day = driver.find_element(By.XPATH, "//div[contains(@class,'react-datepicker__day') and text()='15']")
# day.click()

# 6. Subjects

subjects_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "subjectsInput"))
)

# Method 2: Select from dropdown (more reliable)
subjects_input.send_keys("Comp")
# Wait for dropdown to appear
subject_option = WebDriverWait(driver, 5).until(
    #EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'subjects-auto-complete__option') and contains(text(), 'Computer Science')]"))
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Computer Science')]"))

)
subject_option.click()

time.sleep(2)
# 7. Hobbies (select Sports and Music)
hobbies_sports = driver.find_element(By.XPATH, '//*[@id="hobbies-checkbox-1"]')
driver.execute_script("arguments[0].click();", hobbies_sports)

# hobbies_sports.click()
# hobbies_music = driver.find_element(By.XPATH, "//label[contains(text(),'Music')]")
# hobbies_music.click()

# 8. Upload Picture
upload_picture = driver.find_element(By.ID, "uploadPicture")
upload_picture.send_keys("/Users/jiten/workspace/training/ust-python/pic.png")  # Replace with actual path
## Todo change the path of the photo/pic

# 9. Current Address
address = driver.find_element(By.ID, "currentAddress")
address.send_keys("123 Main Street, Apt 4B, New York, NY 10001")

# 10. State and City
# Scroll to element
state = driver.find_element(By.ID, "state")
driver.execute_script("arguments[0].scrollIntoView();", state)

# Select State
state.click()
state_option = driver.find_element(By.XPATH, "//div[text()='NCR']")
state_option.click()

# Select City
city = driver.find_element(By.ID, "city")
city.click()
city_option = driver.find_element(By.XPATH, "//div[text()='Delhi']")
city_option.click()
#time.sleep(10)
# Submit the form
submit_button = driver.find_element(By.ID, "submit")
submit_button.click()



# Wait for submission and verify
#time.sleep(10)  # Wait for modal to appear

# Validate submission
try:
    success_modal = wait.until(EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg")))
    print("Form submitted successfully!")
    
    # Print submitted data
    submitted_data = driver.find_elements(By.XPATH, "//table//td[2]")
    print("\nSubmitted Data:")
    for data in submitted_data:
        print(data.text)
        
except Exception as e:
    print(f"Form submission failed: {str(e)}")

# Close the browser
driver.quit()