import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage


class OrderPage(BasePage):
    NAME = (By.XPATH, "//input[contains(@placeholder,'Имя')]")
    SURNAME = (By.XPATH, "//input[contains(@placeholder,'Фамилия')]")
    ADDRESS = (By.XPATH, "//input[contains(@placeholder,'Адрес')]")
    METRO = (By.XPATH, "//input[contains(@placeholder,'Станция метро')]")
    METRO_OPTION = "//div[contains(@class,'select-search__select')]//div[text()='{}']"
    PHONE = (By.XPATH, "//input[contains(@placeholder,'Телефон')]")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    DATE = (By.XPATH, "//input[contains(@placeholder,'Когда привезти')]")
    RENT_DROPDOWN = (By.CLASS_NAME, "Dropdown-placeholder")
    RENT_OPTION = "//div[@class='Dropdown-option' and text()='{}']"
    COLOR = {"black": (By.ID, "black"), "grey": (By.ID, "grey")}
    COMMENT = (By.XPATH, "//input[contains(@placeholder,'Комментарий')]")
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class,'Order_Buttons')]//button[text()='Заказать']")

    CONFIRM_YES = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MODAL = (By.XPATH, "//div[contains(@class,'Order_ModalHeader')]")

    @allure.step("Заполнить первый экран формы")
    def fill_first_step(self, name, surname, address, metro, phone):
        self.type_text(self.NAME, name)
        self.type_text(self.SURNAME, surname)
        self.type_text(self.ADDRESS, address)
        self.click(self.METRO)
        self.click((By.XPATH, self.METRO_OPTION.format(metro)))
        self.type_text(self.PHONE, phone)
        self.click(self.NEXT_BUTTON)

    @allure.step("Заполнить второй экран формы")
    def fill_second_step(self, date, rent, color, comment):
        self.type_text(self.DATE, date)
        self.wait_visible(self.DATE).send_keys(Keys.ENTER)
        self.click(self.RENT_DROPDOWN)
        self.click((By.XPATH, self.RENT_OPTION.format(rent)))
        self.click(self.COLOR[color])
        self.type_text(self.COMMENT, comment)
        self.click(self.ORDER_BUTTON)

    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        self.click(self.CONFIRM_YES)

    @allure.step("Получить текст окна об успешном заказе")
    def get_success_text(self):
        return self.get_text(self.SUCCESS_MODAL)