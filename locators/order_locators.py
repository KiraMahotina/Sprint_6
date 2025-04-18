from selenium.webdriver.common.by import By

class OrderPageLocators:
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")

    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.XPATH, "//div[text()='* Срок аренды']")
    PERIOD_OPTION = (By.XPATH, "//div[@class='Dropdown-option' and text()='{}']")
    COLOR_CHECKBOX = (By.ID, "{}")  # Форматируемый локатор для цвета
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")

    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    SUCCESS_POPUP = (By.XPATH, "//div[contains(@class, 'Order_Modal')]")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")

    CHECK_STATUS_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']")
    STATUS_PAGE = (By.XPATH, "//div[contains(@class, 'StatusPage')]")
    STATUS_TITLE = (By.XPATH, "//div[text()='Статус заказа']")
    STATUS_TEXT = (By.XPATH, "//div[@class='Order_Status__']")
