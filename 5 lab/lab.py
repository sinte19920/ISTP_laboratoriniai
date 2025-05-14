import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="class", autouse=True) # function/class/module/session
def browser_fixture(request):
    print(">> Paleidžiama naršyklė")
    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield
    print(">> Uždaroma naršyklė")
    driver.quit()

@pytest.mark.usefixtures("browser_fixture")
class TestRegistration:
    def test_registration1(self):
        self.driver.get("http://suninjuly.github.io/registration1.html")
        self.driver.find_element(By.CSS_SELECTOR, ".first_block .form-control.first").send_keys("Vardenis")
        self.driver.find_element(By.CSS_SELECTOR, ".first_block .form-control.second").send_keys("Pavardenis")
        self.driver.find_element(By.CSS_SELECTOR, ".first_block .form-control.third").send_keys("email@email.com")
        self.driver.find_element(By.CSS_SELECTOR, "button.btn").click()

    def test_registration2_should_fail(self):
        self.driver.get("http://suninjuly.github.io/registration2.html")
        self.driver.find_element(By.CSS_SELECTOR, ".first_block .form-control.first").send_keys("Vardenis")
        self.driver.find_element(By.CSS_SELECTOR, ".first_block .form-control.second").send_keys("Pavardenis")
        self.driver.find_element(By.CSS_SELECTOR, ".first_block .form-control.third").send_keys("email@email.com")
        self.driver.find_element(By.CSS_SELECTOR, "button.btn").click()