from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")
time.sleep(1)

# Clicking the button to open a new window
button = browser.find_element(By.CSS_SELECTOR, "button")
button.click()

# Switching to the new window
original_window = browser.window_handles[0]
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

# Waiting for the input field to appear
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "input_value")))

# Getting the value of x from the page
x_value = browser.find_element(By.ID, "input_value").text
x_value = float(x_value)

# Calculating the answer
answer = math.log(abs(12 * math.sin(x_value)))

# Finding the input field and entering the answer
input_field = browser.find_element(By.ID, "answer")
input_field.send_keys(str(answer))  # Enter the calculated answer

# Waiing until the submit button is enabled and clickable
submit_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']:not([disabled])"))
)

# Checking if the submit button is not disabled
if submit_button.is_enabled():
    submit_button.click()
else:
    print("Submit button is still disabled.")

# Switching to the alert and accepting it
alert = browser.switch_to.alert
alert.accept()
time.sleep(1)

browser.quit()