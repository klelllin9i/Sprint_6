import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ожидание видимости элемента {locator}")
    def wait_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))

    @allure.step("Ожидание кликабельности элемента {locator}")
    def wait_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator))

    @allure.step("Клик по элементу {locator}")
    def click(self, locator):
        element = self.wait_clickable(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    @allure.step("Ввод текста '{text}' в поле {locator}")
    def type_text(self, locator, text):
        self.wait_visible(locator).send_keys(text)

    @allure.step("Получение текста элемента {locator}")
    def get_text(self, locator):
        return self.wait_visible(locator).text

    @allure.step("Ожидание, что URL содержит '{part}'")
    def wait_url_contains(self, part, timeout=15):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(part))

    @allure.step("Ожидание количества окон: {count}")
    def wait_windows_count(self, count, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.number_of_windows_to_be(count))

    @allure.step("Переключение на последнюю вкладку")
    def switch_to_last_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])