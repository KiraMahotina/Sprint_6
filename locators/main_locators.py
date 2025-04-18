from selenium.webdriver.common.by import By

class MainLocators:
    # Локаторы для главной страницы
    SCOOTER_LOGO = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")
    YANDEX_LOGO = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']")
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    TOP_ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button') and text()='Заказать']")
    BOTTOM_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")
