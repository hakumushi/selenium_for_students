from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class HomePage:
    URL='http://www.classedetestes.wordpress.com'
    wait_time_in_seconds = 5
    hidden_options_button = "a.widget-handle.genericon"
    search_field = "s"
    enter_button = "\uE006"

    def __init__(self, driver):
        self.driver = driver

    def open_url(self):
        self.driver.get(self.URL)

    def click_on_menu_item(self, text):
        menu = WebDriverWait(self.driver, self.wait_time_in_seconds).until(
            EC.element_to_be_clickable((By.LINK_TEXT, text)))
        menu.click()

    def click_on_submenu_item(self, text):
        submenu = WebDriverWait(self.driver, self.wait_time_in_seconds).until(
            EC.element_to_be_clickable((By.LINK_TEXT, text.upper())))
        submenu.click()

    def open_hidden_options(self):
        field = WebDriverWait(self.driver, self.wait_time_in_seconds).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.hidden_options_button)))
        field.click()

    def search_for(self, text):
        field = WebDriverWait(self.driver, self.wait_time_in_seconds).until(
            EC.visibility_of_element_located((By.NAME, self.search_field)))
        field.clear()
        field.send_keys(text)
        field.send_keys(self.enter_button)

    def get_header(self, class_name):
        return self.driver.find_element(By.CLASS_NAME, class_name).text

    def get_page_title(self):
        return self.driver.title
