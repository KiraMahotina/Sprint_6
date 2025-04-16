from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.question_locators import QuestionLocators
import allure


class QuestionPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Кликнуть на вопрос с ID {question_id}")
    def click_question(self, question_id):
        locator = (QuestionLocators.QUESTION[0], QuestionLocators.QUESTION[1].format(question_id))
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).click()

    @allure.step("Получить текст ответа для вопроса с ID {question_id}")
    def get_answer_text(self, question_id):
        locator = (QuestionLocators.ANSWER[0], QuestionLocators.ANSWER[1].format(question_id))
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        ).text
