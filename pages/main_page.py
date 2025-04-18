from .base_page import BasePage
from locators.main_locators import MainLocators
from curl import Curls
import allure

class MainPage(BasePage):
    @allure.step("Открыть главную страницу")
    def open(self):
        self.driver.get(Curls.MAIN_PAGE)
        self.close_cookie_banner()

    @allure.step("Закрыть баннер с куки")
    def close_cookie_banner(self):
        self.click_element(MainLocators.COOKIE_BUTTON)

    @allure.step("Нажать кнопку 'Заказать' ({button_type})")
    def click_order_button(self, button_type):
        locator = (
            MainLocators.TOP_ORDER_BUTTON
            if button_type == "top"
            else MainLocators.BOTTOM_ORDER_BUTTON
        )
        self.click_element(locator)

    @allure.step("Нажать на логотип Самоката")
    def click_scooter_logo(self):
        self.click_element(MainLocators.SCOOTER_LOGO)

    @allure.step("Нажать на логотип Яндекса")
    def click_yandex_logo(self):
        self.click_element(MainLocators.YANDEX_LOGO)
