from .base_page import BasePage
from locators.question_locators import QuestionLocators
import allure

class QuestionPage(BasePage):
    @allure.step("Кликнуть на вопрос с ID {question_id}")
    def click_question(self, question_id):
        locator = (QuestionLocators.QUESTION[0], QuestionLocators.QUESTION[1].format(question_id))
        self.click_element(locator)

    @allure.step("Получить текст ответа для вопроса с ID {question_id}")
    def get_answer_text(self, question_id):
        locator = (QuestionLocators.ANSWER[0], QuestionLocators.ANSWER[1].format(question_id))
        return self.wait_for_element(locator).text