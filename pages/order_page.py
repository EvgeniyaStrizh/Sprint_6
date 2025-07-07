from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrderPage:
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
        self.driver = driver

    def fill_personal_info(self, name, surname, address, station, phone):
        self.driver.find_element(*self.NAME).send_keys(name)
        self.driver.find_element(*self.SURNAME).send_keys(surname)
        self.driver.find_element(*self.ADDRESS).send_keys(address)
        self.driver.find_element(*self.STATION).send_keys(station)
        self.driver.find_element(By.XPATH, f"//button/div[text()='{station}']").click()
        self.driver.find_element(*self.PHONE).send_keys(phone)
        self.driver.find_element(*self.NEXT_BTN).click()

    def fill_order_info(self, date, comment):
        self.driver.find_element(*self.DATE).send_keys(date)
        self.driver.find_element(*self.HEADING).click()
        self.driver.find_element(*self.RENT_DROPDOWN).click()
        self.driver.find_element(*self.RENT_OPTION).click()
        self.driver.find_element(*self.COLOR_CHECKBOX).click()
        self.driver.find_element(*self.COMMENT).send_keys(comment)
        self.driver.find_element(*self.ORDER_BTN).click()
        self.driver.find_element(*self.CONFIRM_BTN).click()

    def is_order_successful(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.SUCCESS_MODAL)
        ).is_displayed()
