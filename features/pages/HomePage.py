from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class HomePage(BasePage):
    URL='http://www.classedetestes.wordpress.com'
    HIDDEN_OPTIONS_BUTTON = (By.CSS_SELECTOR, "a.widget-handle.genericon")
    SEARCH_FIELD = (By.NAME, "s")
    HOME_MENU_ITEM = (By.CSS_SELECTOR, '#menu-item-103')
    CSS_SELENIUM = (By.CSS_SELECTOR, '#menu-item-6 > a')
    CSS_CURSO_SELENIUM = (By.CSS_SELECTOR, '#menu-item-52')
    CSS_FORMULARIO = (By.CSS_SELECTOR, '#menu-item-51')
    ENTRY_TITLE = (By.CLASS_NAME, 'entry-title')
    PAGE_TITLE = (By.CLASS_NAME, 'page-title')

    def open_classedetestes(self):
        super().open_url(self.URL)

    def get_page_title(self):
        return super().get_title()

    def click_on_home_screen_link(self):
        super().click(self.HOME_MENU_ITEM)

    def click_on_selenium_link(self):
        super().click(self.CSS_SELENIUM)

    def click_on_curso_selenium_link(self):
        super().click(self.CSS_CURSO_SELENIUM)

    def click_on_formulario_link(self):
        super().click(self.CSS_FORMULARIO)

    def open_hidden_options(self):
        super().click(self.HIDDEN_OPTIONS_BUTTON)

    def search_for(self, text):
        super().type_in(self.SEARCH_FIELD,text)
        super().type_in(self.SEARCH_FIELD,Keys.RETURN, False)

    def get_header_of_a_entry_title(self):
        return super().find(self.ENTRY_TITLE).text

    def get_header_of_a_page_title(self):
        return super().find(self.PAGE_TITLE).text
