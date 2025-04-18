import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import Data
from curl import Curls


class TestOrderFlow:
    @allure.title("Оформление заказа с данными: {data}")
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
        assert main_page.get_current_url() == Curls.MAIN_PAGE

        main_page.click_yandex_logo()

        main_page.switch_to_window(1)

        main_page.wait_for_url_contains(Curls.DZEN_PAGE, timeout=15)
        assert Curls.DZEN_PAGE in main_page.get_current_url()
