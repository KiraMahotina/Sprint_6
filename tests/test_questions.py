import pytest
from data import Data
from pages.main_page import MainPage
from pages.question_page import QuestionPage
import allure


class TestQuestions:
    @allure.title("Проверка ответа на вопрос #{question_id}")
    @pytest.mark.parametrize('question_id, expected_answer', Data.QUESTION_ANSWERS)
    def test_question_answer(self, driver, question_id, expected_answer):
        main_page = MainPage(driver)
        main_page.open()

        question_page = QuestionPage(driver)
        question_page.click_question(question_id)
        actual_answer = question_page.get_answer_text(question_id)

        assert actual_answer == expected_answer, f"Ожидался ответ: {expected_answer}, получен: {actual_answer}"
