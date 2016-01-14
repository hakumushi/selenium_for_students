from time import time

class Utils:

    path = '/home/mushi720/Documents/BDD/selenium_for_students/Screenshots/'

    def __init__(self, driver):
        self.driver = driver

    def time_code(self):
        return str(time()).replace(".", "")

    def take_a_screenshot(self, file_name):
        self.driver.get_screenshot_as_file(self.path + file_name + self.time_code() )
