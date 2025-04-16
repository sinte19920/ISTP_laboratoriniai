from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)

book_btn = browser.find_element(By.ID, "book")
book_btn.click()

x = browser.find_element(By.ID, "input_value").text
answer = calc(x)

input_field = browser.find_element(By.ID, "answer")
input_field.send_keys(answer)

submit_btn = browser.find_element(By.ID, "solve")
submit_btn.click()