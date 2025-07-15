from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import allure


class MainPage(BasePage):
    URL = "https://qa-scooter.praktikum-services.ru/"

    QUESTIONS = (By.CLASS_NAME, "accordion__button")
    LOGO_SCOOTER = (By.CSS_SELECTOR, "a[class*='Header_LogoScooter']")
    LOGO_YANDEX = (By.CSS_SELECTOR, "a[class*='Header_LogoYandex']")
    UPPER_ORDER_BTN = (By.XPATH, "(//button[text()='Заказать'])[1]")
    LOWER_ORDER_BTN = (By.XPATH, "(//button[text()='Заказать'])[2]")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Отркыть главную страницу")
    def open(self):
        super().open(self.URL)

    @allure.step("Кликнуть на вопрос с индексом {index}")
    def click_question(self, index):
        question = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, f"accordion__heading-{index}"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'start'});", question)

        actions = ActionChains(self.driver)
        actions.move_to_element(question).click().perform()

    def get_answer_text(self, index):
        locator = (By.ID, f"accordion__panel-{index}")
        answer = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        return answer.text

    @allure.step("Нажать на кнопку Заказать")
    def click_order_button(self, position='top'):
        button = self.UPPER_ORDER_BTN if position == 'top' else self.LOWER_ORDER_BTN
        if button is self.LOWER_ORDER_BTN:
            element_button = self.driver.find_element(*button)
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'start'});", element_button)
            actions = ActionChains(self.driver)
            actions.move_to_element(element_button).click().perform()
        else:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(button)).click()

    def click_logo_scooter(self):
        self.click(*self.LOGO_SCOOTER)

    def click_logo_yandex(self):
        self.click(*self.LOGO_YANDEX)
