import allure
import pytest
from pages.main_page import MainPage
from data import FAQ_DATA


@allure.feature("Раздел «Вопросы о важном»")
class TestFaq:
    @allure.title("Ответ на вопрос №{index} раскрывается")
    @pytest.mark.parametrize("index, expected", FAQ_DATA)
    def test_answer_opens(self, driver, index, expected):
        page = MainPage(driver)
        page.accept_cookies()
        assert page.open_question_get_answer(index) == expected