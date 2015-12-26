from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class HomePage:
    URL='http://www.classedetestes.wordpress.com'
    wait_time_in_seconds = 5 #O WebDriverWait ignora NotFoundExceptions por 5 segundos

    def __init__(self, driver):
        self.driver = driver

    def open_url(self):
        self.driver.get(self.URL)

    def link_click(self, text):
        button = WebDriverWait(self.driver, self.wait_time_in_seconds).until(
            EC.visibility_of_element_located((By.LINK_TEXT, text)))
        button.click()

    def click_on_menu_item(self, text):
        menu = WebDriverWait(self.driver, self.wait_time_in_seconds).until(
            EC.element_to_be_clickable((By.LINK_TEXT, text)))
        menu.click()

    def click_on_submenu_item(self, text):
        submenu = WebDriverWait(self.driver, self.wait_time_in_seconds).until(
            EC.element_to_be_clickable((By.LINK_TEXT, text)))
        submenu.click()

    def get_header(self, class_name):
        return self.driver.find_element(By.CLASS_NAME, class_name).text

    def get_page_title(self):
        return self.driver.title
