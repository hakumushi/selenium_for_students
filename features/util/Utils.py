class Utils:

    path = '/home/mushi720/Documents/BDD/selenium_for_students/Screenshots/'

    def __init__(self, driver):
        self.driver = driver

    def take_a_screenshot(self):
        self.driver.get_screenshot_as_file(self.path+'file_name')
