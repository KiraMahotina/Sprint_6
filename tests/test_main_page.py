from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from curl import Curls

def test_scooter_logo_redirect(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_scooter_logo()
    assert driver.current_url == Curls.MAIN_PAGE


def test_yandex_logo_redirect(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_yandex_logo()
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 10).until(EC.url_contains(Curls.DZEN_PAGE))
    assert driver.current_url == Curls.DZEN_PAGE
