from pages.main_page import MainPage
from curl import Curls
import allure


class TestMainPage:
    @allure.title("Проверка редиректа по логотипу Самоката")
    def test_scooter_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_scooter_logo()
        assert main_page.get_current_url() == Curls.MAIN_PAGE

    @allure.title("Проверка редиректа на Яндекс.Дзен")
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_yandex_logo()
        main_page.switch_to_window(1)
        main_page.wait_for_url_contains(Curls.DZEN_PAGE)
        assert main_page.get_current_url() == Curls.DZEN_PAGE
