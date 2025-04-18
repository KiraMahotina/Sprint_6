from selenium.webdriver.common.by import By

class QuestionLocators:
    QUESTION = (By.ID, "accordion__heading-{}")
    ANSWER = (By.ID, "accordion__panel-{}")
