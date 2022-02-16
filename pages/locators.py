from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_BASKET = (By.CSS_SELECTOR, ".btn-group")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, ".basket-title.hidden-xs")
    TEXT_BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#register_form")
    FIELD_REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#register_form [name='registration-email']")
    FIELD_REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#register_form [name='registration-password1']")
    FIELD_REGISTRATION_REPEAT_PASSWORD = (By.CSS_SELECTOR, "#register_form [name='registration-password2']")
    BUTTON_REGISTRATION = (By.CSS_SELECTOR, "#register_form [name='registration_submit']")

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form")
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert:nth-child(1) > .alertinner > strong")
    BASKET_VALUE_IN_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert-info > .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert:nth-child(1)")
