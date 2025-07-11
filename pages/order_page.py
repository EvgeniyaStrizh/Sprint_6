from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class OrderPage(BasePage):

    NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    STATION = (By.CLASS_NAME, "select-search__input")
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BTN = (By.XPATH, "//button[text()='Далее']")

    HEADING = (By.XPATH, "//*[contains(@class, 'Order_Header')]")
    DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT_DROPDOWN = (By.CLASS_NAME, "Dropdown-control")
    RENT_OPTION = (By.XPATH, "//div[@class='Dropdown-menu']//div[text()='сутки']")
    COLOR_CHECKBOX = (By.ID, "black")  # Пример
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BTN = (By.XPATH, "(//button[text()='Заказать'])[2]")
    CONFIRM_BTN = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MODAL = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        super().open(self.URL)

    def fill_personal_info(self, name, surname, address, station, phone):
        self.send_keys(*self.NAME, name)
        self.send_keys(*self.SURNAME, surname)
        self.send_keys(*self.ADDRESS, address)
        self.send_keys(*self.STATION, station)
        self.click((By.XPATH, f"//button/div[text()='{station}']"))
        self.driver.find_element(*self.PHONE).send_keys(phone)
        self.click(*self.NEXT_BTN)

    def fill_order_info(self, date, comment):
        self.send_keys(*self.DATE, date)
        self.click(*self.HEADING)
        self.click(*self.RENT_DROPDOWN)
        self.click(*self.RENT_OPTION)
        self.click(*self.COLOR_CHECKBOX)
        self.send_keys(*self.COMMENT, comment)
        self.click(*self.ORDER_BTN)
        self.click(*self.CONFIRM_BTN)

    def is_order_successful(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.SUCCESS_MODAL)
        ).is_displayed()
