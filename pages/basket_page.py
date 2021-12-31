from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_no_product_in_basket(self):  # в корзине не должно быть товаров
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), \
            "Product is in the basket, but should not"

    def presence_of_text_about_an_empty_basket(self):  # наличие текста о пустой корзине
        text = self.browser.find_element(*BasketPageLocators.TEXT_BASKET_IS_EMPTY).text
        assert 'Your basket is empty.' in text, \
            "No text about empty basket"
