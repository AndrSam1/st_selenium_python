import pytest

from .pages.basket_page import BasketPage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    # Гость открывает главную страницу
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    # Переходит в корзину по кнопке в шапке сайта
    page.guest_clik_button_see_basket()
    basket_page = BasketPage(browser, browser.current_url)
    # Ожидаем, что в корзине нет товаров
    basket_page.should_be_basket_is_empty()
    # Ожидаем, что есть текст о том что корзина пуста
    basket_page.should_be_text_basket_is_empty()