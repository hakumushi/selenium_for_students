from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class HomePage:
    URL='http://www.classedetestes.wordpress.com'
    WAIT_TIME_IN_SECONDS = 5
    HIDDEN_OPTIONS_BUTTON = "a.widget-handle.genericon"
    SEARCH_FIELD = "s"
    HOME_MENU_ITEM = '#menu-item-103'
    CSS_SELENIUM = '#menu-item-6 > a'
    CSS_CURSO_SELENIUM = '#menu-item-52'
    CSS_FORMULARIO = '#menu-item-51'
    ENTRY_TITLE = 'entry-title'
    PAGE_TITLE = 'page-title'

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.WAIT_TIME_IN_SECONDS)

    def open_url(self):
        self.driver.get(self.URL)

    def click_on_home_screen_link(self):
        menu = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.HOME_MENU_ITEM)))
        menu.click()

    def click_on_selenium_link(self):
        menu = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.CSS_SELENIUM)))
        menu.click()

    def click_on_curso_selenium_link(self):
        menu = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.CSS_CURSO_SELENIUM)))
        menu.click()

    def click_on_formulario_link(self):
        menu = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.CSS_FORMULARIO)))
        menu.click()

    def open_hidden_options(self):
        menu = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.HIDDEN_OPTIONS_BUTTON)))
        menu.click()

    def search_for(self, text):
        field = self.wait.until(EC.visibility_of_element_located((By.NAME, self.SEARCH_FIELD)))
        field.clear()
        field.send_keys(text)
        field.send_keys(Keys.RETURN)

    def get_header_of_a_entry_title(self):
        return self.driver.find_element(By.CLASS_NAME, self.ENTRY_TITLE).text

    def get_header_of_a_page_title(self):
        return self.driver.find_element(By.CLASS_NAME, self.PAGE_TITLE).text

    def get_page_title(self):
        return self.driver.title
