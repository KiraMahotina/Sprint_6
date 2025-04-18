from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Кликнуть на элемент {locator}")
    def click_element(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    @allure.step("Ввести текст '{text}' в элемент {locator}")
    def send_keys_to_element(self, locator, text, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        element.send_keys(text)

    @allure.step("Ожидать видимости элемента {locator}")
    def wait_for_element(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Ожидать URL, содержащего '{url}'")
    def wait_for_url_contains(self, url, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(url))

    @allure.step("Переключиться на окно с индексом {window_index}")
    def switch_to_window(self, window_index):
        self.driver.switch_to.window(self.driver.window_handles[window_index])

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url
