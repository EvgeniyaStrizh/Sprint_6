from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until()

    def click(self, locator):
        self.driver.find_element(locator).click()

    def send_keys(self, locator, text):
        self.driver.find_element(locator).send_keys(text)

    def close_cookies_banner(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            ).click()
        except:
            pass
