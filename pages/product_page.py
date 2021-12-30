from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def adding_an_product_to_basket(self):  # добавление товара в корзину
        self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET).click()

    def check_product_name_in_message(self):  # проверка название товара в сообщении
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text
        assert product_name == product_name_in_message, "Product name in the message is not correct  Название продукта в сообщении неверно"

    def checking_value_of_basket_in_message(self):  # проверка стоимости корзины в сообщении
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_value_in_message = self.browser.find_element(*ProductPageLocators.BASKET_VALUE_IN_MESSAGE).text
        assert product_price == basket_value_in_message, "The cost of the basket does not match the price of the product  Стоимость корзины не соответствует цене товара"