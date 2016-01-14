from selenium import webdriver
from util.Utils import Utils
import os

def before_all(context):
    context.driver = webdriver.Chrome(executable_path=os.path.dirname(os.path.realpath(__file__)) + "/resources/chromedriver")
    #context.driver = webdriver.Firefox()
    context.driver.implicitly_wait(30)
    context.driver.maximize_window()
    context.utils = Utils(context.driver)

def after_scenario(context, scenario):
    context.utils.take_a_screenshot('Teste')

def after_all(context):
    context.driver.close()
