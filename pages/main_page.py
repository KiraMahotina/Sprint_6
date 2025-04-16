from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_locators import MainLocators
from curl import Curls
import allure


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть главную страницу")
    def open(self):
        self.driver.get(Curls.MAIN_PAGE)
        self.close_cookie_banner()

    @allure.step("Закрыть баннер с куки")
    def close_cookie_banner(self):
        self.driver.find_element(*MainLocators.COOKIE_BUTTON).click()

    @allure.step("Нажать кнопку 'Заказать' ({button_type})")
    def click_order_button(self, button_type):
        if button_type == "top":
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(MainLocators.TOP_ORDER_BUTTON)
            ).click()
        else:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(MainLocators.BOTTOM_ORDER_BUTTON)
            ).click()

    @allure.step("Нажать на логотип Самоката")
    def click_scooter_logo(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainLocators.SCOOTER_LOGO)
        )
        element.click()

    @allure.step("Нажать на логотип Яндекса")
    def click_yandex_logo(self):
        self.driver.find_element(*MainLocators.YANDEX_LOGO).click()