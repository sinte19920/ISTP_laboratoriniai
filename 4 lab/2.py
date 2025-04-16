import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestRegistration(unittest.TestCase):

    def fill_form_and_check_success(self, url):
        browser = webdriver.Chrome()
        browser.get(url)

        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first").send_keys("Vardenis")
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second").send_keys("Pavardenis")
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third").send_keys("test@test.com")

        time.sleep(2)

        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        time.sleep(1)
        success_text = browser.find_element(By.TAG_NAME, "h1").text
        browser.quit()
        return success_text

    def test_registration1_should_pass(self):
        text = self.fill_form_and_check_success("http://suninjuly.github.io/registration1.html")
        self.assertEqual(text, "Congratulations! You have successfully registered!")
        time.sleep(1)

    def test_registration2_should_fail(self):
        text = self.fill_form_and_check_success("http://suninjuly.github.io/registration2.html")
        self.assertEqual(text, "Congratulations! You have successfully registered!")

if __name__ == "__main__":
    unittest.main()