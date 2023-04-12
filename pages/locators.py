from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group>a.btn.btn-default")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, ".alert-success.fade.in:nth-child(1) .alertinner strong")
    PRODUCT_BASKET_AMOUNT = (By.CSS_SELECTOR, ".alert-info.fade.in .alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success.fade.in:nth-child(1)")

class BasketPageLocators():
    TEXT_BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner>p")
    BASKET_ITEMS = (By.CLASS_NAME, "basket-items")

