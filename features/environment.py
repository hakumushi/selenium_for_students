from selenium import webdriver
import os

def before_all(context):
    context.driver = webdriver.Chrome(executable_path=os.path.dirname(os.path.realpath(__file__)) + "/resources/chromedriver")
    context.driver.implicitly_wait(30)
    context.driver.maximize_window()

def after_all(context):
    context.driver.close()
