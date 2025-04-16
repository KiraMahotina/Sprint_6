from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.order_locators import OrderPageLocators
from selenium.webdriver.common.by import By
from curl import Curls
import allure


class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Заполнить форму заказа")
    def fill_order_form(self, name, surname, address, metro, phone, date, period, color, comment):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrderPageLocators.NAME_INPUT)
        ).send_keys(name)

        self.driver.find_element(*OrderPageLocators.SURNAME_INPUT).send_keys(surname)
        self.driver.find_element(*OrderPageLocators.ADDRESS_INPUT).send_keys(address)

        # Выбор станции метро
        metro_input = self.driver.find_element(*OrderPageLocators.METRO_INPUT)
        metro_input.click()
        metro_input.send_keys(metro)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f"//div[text()='{metro}']"))
        ).click()

        self.driver.find_element(*OrderPageLocators.PHONE_INPUT).send_keys(phone)
        self.driver.find_element(*OrderPageLocators.NEXT_BUTTON).click()


        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(@class, 'Order_Header__BZXOb') and text()='Про аренду']"))
        )

        date_input = self.driver.find_element(*OrderPageLocators.DATE_INPUT)
        date_input.click()
        date_input.send_keys(date)

        selected_date_locator = (By.XPATH, "//div[contains(@class, 'react-datepicker__day--selected')]")

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(selected_date_locator)
        ).click()

        period_input = self.driver.find_element(*OrderPageLocators.RENTAL_PERIOD_DROPDOWN)

        period_input.click()

        period_locator = (By.XPATH, f"//div[@class='Dropdown-option' and text()='{period}']")
        option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(period_locator)
        )
        option.click()

        if color:
            self.driver.find_element(By.ID, color).click()

        if comment:
            comment_field = self.driver.find_element(*OrderPageLocators.COMMENT_INPUT)
            comment_field.send_keys(comment)

        self.driver.find_element(*OrderPageLocators.ORDER_BUTTON).click()


    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(OrderPageLocators.CONFIRM_BUTTON)
        ).click()

        # Ожидаем появление попапа успешного заказа
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(OrderPageLocators.SUCCESS_POPUP)
        )

    @allure.step("Проверить успешное оформление заказа")
    def is_success_popup_displayed(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrderPageLocators.SUCCESS_POPUP)
        )

        check_status_button_locator = OrderPageLocators.CHECK_STATUS_BUTTON
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(check_status_button_locator)
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.url_contains(Curls.STATUS_PAGE)
        )
        return True
