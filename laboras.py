from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://www.tutorialspoint.com/selenium/practice/register.php"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element(By.ID, "firstname")
input1.send_keys("Vardas")
time.sleep(2)
input1 = browser.find_element(By.ID, "lastname")
input1.send_keys("Pavarde")
time.sleep(2)
input1 = browser.find_element(By.ID, "username")
input1.send_keys("Vartotojo Vardas")
time.sleep(2)
input1 = browser.find_element(By.ID, "password")
input1.send_keys("slaptazodis")
time.sleep(2)

button = browser.find_element(By.CLASS_NAME, "btn")
button.click()