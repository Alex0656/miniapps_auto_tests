from pages.elements_page import TextBoxPage
import time


class TestElements:
    class TestTextBox:
        def test_text_box(self, driver):
            page = TextBoxPage(driver, 'https://test.miniapps.kreosoft.space/')
            page.open()
            page.fill_all_field()