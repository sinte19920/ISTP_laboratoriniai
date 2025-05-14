import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# fixture paleidžia ir uždaro web kiekvienam testui
@pytest.fixture
def browser():
    print("\n[SETUP] Start browser for test...")
    browser = webdriver.Chrome()
    yield browser
    print("\n[TEARDOWN] Quit browser...")
    browser.quit()

class TestRegistration:
    def test_registration_form1(self, browser):
        link = "http://suninjuly.github.io/registration1.html"
        browser.get(link)

        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first").send_keys("Lila")
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second").send_keys("Adomaitytė")
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third").send_keys("lila@example.com")

        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        time.sleep(1)

        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        assert welcome_text == "Congratulations! You have successfully registered!", \
            "Form 1: Registration failed"

    def test_registration_form2(self, browser):
        link = "http://suninjuly.github.io/registration2.html"
        browser.get(link)

        try:
            browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first").send_keys("Lila")
            browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third").send_keys("lila@example.com")
        except NoSuchElementException as e:
            print("Vienas iš laukų nerastas:", e)
            assert False, "Testas nutrūko – negalima rasti privalomo lauko."

        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        try:
            welcome_text_element = WebDriverWait(browser, 5).until(
                EC.visibility_of_element_located((By.TAG_NAME, "h1"))
            )
            welcome_text = welcome_text_element.text
            assert "Congratulations! You have successfully registered!" in welcome_text
        except Exception as e:
            print("Nepavyko rasti rezultatų antraštės:", e)
            assert False, "Testas nepavyko – rezultatų tekstas nerastas arba yra nurodytas neteisingas."
