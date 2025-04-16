from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/alert_accept.html")

# Clicking the button to trigger the alert
button = browser.find_element(By.CSS_SELECTOR, "button")
button.click()
time.sleep(1)

# Switching to the alert and accepting it
alert = browser.switch_to.alert
alert.accept()
time.sleep(1)

# Waiting for the input field to appear
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "input_value")))
time.sleep(1)

# Getting the value of x from the page
x_value = browser.find_element(By.ID, "input_value").text
x_value = float(x_value)  # Convert the value to a float

# Calculating the answer for the formula
answer = math.log(abs(12 * math.sin(x_value)))

# Finding the input field and entering the answer
input_field = browser.find_element(By.ID, "answer")
input_field.send_keys(str(answer))  # Enter the calculated answer

# Submitting the form
submit_button = browser.find_element(By.CSS_SELECTOR, "button.submit")
submit_button.click()

browser.quit()