from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form")
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert:nth-child(1) > .alertinner > strong")
    BASKET_VALUE_IN_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert-info > .alertinner strong")