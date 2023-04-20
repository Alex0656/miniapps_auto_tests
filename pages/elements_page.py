import time

from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_field(self):
        self.element_is_visible(self.locators.EMAIL).send_keys('waywwwwalex1@rambler.ru')
        self.element_is_visible(self.locators.PASSWORD).send_keys('12345678')
        self.element_is_clickable(self.locators.OPEN).click()
        time.sleep(5)