import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    ORDER_BUTTON_TOP = (By.XPATH, "//div[contains(@class,'Header_Nav')]//button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class,'Home_FinishButton')]//button[text()='Заказать']")
    LOGO_SCOOTER = (By.XPATH, "//a[contains(@class,'Header_LogoScooter')]")
    LOGO_YANDEX = (By.XPATH, "//a[contains(@class,'Header_LogoYandex')]")

    QUESTION = "accordion__heading-{}"
    ANSWER = "accordion__panel-{}"

    @allure.step("Принять cookie")
    def accept_cookies(self):
        self.click(self.COOKIE_BUTTON)

    @allure.step("Открыть вопрос №{index} и получить текст ответа")
    def open_question_get_answer(self, index):
        self.click((By.ID, self.QUESTION.format(index)))
        return self.get_text((By.ID, self.ANSWER.format(index)))

    @allure.step("Нажать кнопку «Заказать» ({position})")
    def click_order(self, position):
        locator = self.ORDER_BUTTON_TOP if position == "top" else self.ORDER_BUTTON_BOTTOM
        self.click(locator)

    @allure.step("Нажать на логотип Самоката")
    def click_scooter_logo(self):
        self.click(self.LOGO_SCOOTER)

    @allure.step("Нажать на логотип Яндекса")
    def click_yandex_logo(self):
        self.click(self.LOGO_YANDEX)