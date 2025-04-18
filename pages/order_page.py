from .base_page import BasePage
from locators.order_locators import OrderPageLocators
from selenium.webdriver.common.by import By
from curl import Curls
import allure


class OrderPage(BasePage):
    @allure.step("Заполнить форму заказа")
    def fill_order_form(self, name, surname, address, metro, phone, date, period, color, comment):
        self.send_keys_to_element(OrderPageLocators.NAME_INPUT, name)
        self.send_keys_to_element(OrderPageLocators.SURNAME_INPUT, surname)
        self.send_keys_to_element(OrderPageLocators.ADDRESS_INPUT, address)

        # Выбор метро
        self.click_element(OrderPageLocators.METRO_INPUT)
        metro_locator = (By.XPATH, f"//div[text()='{metro}']")
        self.click_element(metro_locator)

        self.send_keys_to_element(OrderPageLocators.PHONE_INPUT, phone)
        self.click_element(OrderPageLocators.NEXT_BUTTON)

        self.wait_for_element((By.XPATH, "//div[contains(text(), 'Про аренду')]"))

        self.send_keys_to_element(OrderPageLocators.DATE_INPUT, date)
        self.click_element((By.XPATH, "//div[contains(@class, 'react-datepicker__day--selected')]"))

        self.click_element(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        period_locator = (By.XPATH, f"//div[text()='{period}']")
        self.click_element(period_locator)

        if color:
            self.click_element((By.ID, color))

        if comment:
            self.send_keys_to_element(OrderPageLocators.COMMENT_INPUT, comment)

        self.click_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        self.click_element(OrderPageLocators.CONFIRM_BUTTON, timeout=15)
        self.wait_for_element(OrderPageLocators.SUCCESS_POPUP, timeout=15)

    @allure.step("Проверить успешное оформление заказа")
    def is_success_popup_displayed(self):
        self.wait_for_element(OrderPageLocators.SUCCESS_POPUP)
        self.click_element(OrderPageLocators.CHECK_STATUS_BUTTON)
        self.wait_for_url_contains(Curls.STATUS_PAGE, timeout=20)
        return True
