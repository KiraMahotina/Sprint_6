import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import Data
from curl import Curls
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.order_locators import OrderPageLocators
from selenium.webdriver.common.by import By


class TestOrderFlow:
    @pytest.mark.parametrize('data', Data.TEST_DATA)
    def test_complete_order_flow(self, driver, data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.open()
        main_page.click_order_button(data['button'])
        order_page.fill_order_form(
                data['name'],
                data['surname'],
                data['address'],
                data['metro'],
                data['phone'],
                data['date'],
                data['period'],
                data['color'],
                data['comment']
            )

        order_page.confirm_order()
        assert order_page.is_success_popup_displayed()

        main_page.click_scooter_logo()
        assert driver.current_url == Curls.MAIN_PAGE

        main_page.click_yandex_logo()
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[1])


        WebDriverWait(driver, 15).until(EC.url_contains(Curls.DZEN_PAGE))
        assert Curls.DZEN_PAGE in driver.current_url
