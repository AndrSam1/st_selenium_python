from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_text_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_BASKET_IS_EMPTY), \
            "There is no text that the basket is empty"

    def should_be_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "The basket is not empty, but should be"
