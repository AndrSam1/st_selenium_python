from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        login_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        login_link.click()

    def should_be_product_in_basket(self):
        # проверка добавления товара в корзину
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == \
               self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET).text, \
            "The product name does not match the one added"

    def should_be_amount_basket(self):
        # проверка суммы корзины
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text == \
               self.browser.find_element(*ProductPageLocators.PRODUCT_BASKET_AMOUNT).text, \
            "The product price does not match the basket amount"


