import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import ORDER_DATA


@allure.feature("Заказ самоката")
class TestOrder:
    @allure.title("Позитивный сценарий заказа через кнопку «{entry}»")
    @pytest.mark.parametrize(
        "entry, name, surname, address, metro, phone, date, rent, color, comment",
        ORDER_DATA)
    def test_order_flow(self, driver, entry, name, surname, address, metro,
                        phone, date, rent, color, comment):
        main = MainPage(driver)
        order = OrderPage(driver)
        main.accept_cookies()
        main.click_order(entry)
        order.fill_first_step(name, surname, address, metro, phone)
        order.fill_second_step(date, rent, color, comment)
        order.confirm_order()
        assert "Заказ оформлен" in order.get_success_text()

    @allure.title("Клик по логотипу Самоката ведёт на главную")
    def test_scooter_logo(self, driver):
        main = MainPage(driver)
        main.accept_cookies()
        main.click_order("top")
        main.click_scooter_logo()
        main.wait_url_contains("qa-scooter.praktikum-services.ru")
        assert driver.current_url.rstrip("/").endswith("praktikum-services.ru")

    @allure.title("Клик по логотипу Яндекса открывает Дзен в новом окне")
    def test_yandex_logo(self, driver):
        main = MainPage(driver)
        main.accept_cookies()
        main.click_yandex_logo()
        main.wait_windows_count(2)
        main.switch_to_last_window()
        main.wait_url_contains("dzen.ru")
        assert "dzen.ru" in driver.current_url