from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class HomePage:
    URL='http://www.classedetestes.wordpress.com'
    WAIT_TIME_IN_SECONDS = 5
    HIDDEN_OPTIONS_BUTTON = "a.widget-handle.genericon"
    SEARCH_FIELD = "s"

    def __init__(self, driver):
        self.driver = driver

    def open_url(self):
        self.driver.get(self.URL)

    def click_on_link(self, selector):
        menu = WebDriverWait(self.driver, self.WAIT_TIME_IN_SECONDS).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
        menu.click()

    def search_for(self, text):
        field = WebDriverWait(self.driver, self.WAIT_TIME_IN_SECONDS).until(
            EC.visibility_of_element_located((By.NAME, self.SEARCH_FIELD)))
        field.clear()
        field.send_keys(text)
        field.send_keys(Keys.RETURN)

    def get_header(self, class_name):
        return self.driver.find_element(By.CLASS_NAME, class_name).text

    def get_page_title(self):
        return self.driver.title
