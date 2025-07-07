import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage

order_data = [
    ("Иван", "Иванов", "Москва, Тверская", "Сокол", "89112223344", "10.07.2025", "Позвоните заранее"),
    ("Ольга", "Петрова", "Москва, Арбат", "Черкизовская", "89997775566", "11.07.2025", "Поставьте у подъезда"),
]

@pytest.mark.parametrize("name, surname, address, station, phone, date, comment", order_data)
@pytest.mark.parametrize("button_position", ['top', 'bottom'])
def test_order_flow(driver, name, surname, address, station, phone, date, comment, button_position):
    main = MainPage(driver)
    main.open()
    main.click_order_button(position=button_position)

    order = OrderPage(driver)
    order.fill_personal_info(name, surname, address, station, phone)
    order.fill_order_info(date, comment)
    assert order.is_order_successful()
