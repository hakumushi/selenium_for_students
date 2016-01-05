from pages.HomePage import HomePage
from hamcrest import assert_that, equal_to

HOME_MENU_ITEM = '#menu-item-103'
CSS_SELENIUM = '#menu-item-6 > a'
CSS_CURSO_SELENIUM = '#menu-item-52'
CSS_FORMULARIO = '#menu-item-51'
HIDDEN_OPTIONS_BUTTON = "a.widget-handle.genericon"

@given(u'I am on Home Page')
def step_impl(context):
    context.page_object = HomePage(context.driver)
    context.page_object.open_url()

@when(u'I open the home screen')
def step_impl(context):
    context.page_object.click_on_link(HOME_MENU_ITEM)

@when(u'I click on sub menu item Curso Selenium')
def step_impl(context):
    context.page_object.click_on_link(CSS_SELENIUM)
    context.page_object.click_on_link(CSS_CURSO_SELENIUM)

@when(u'I click on sub menu item Formulario Simples')
def step_impl(context):
    context.page_object.click_on_link(CSS_SELENIUM)
    context.page_object.click_on_link(CSS_FORMULARIO)

@when(u'I search for "{text}"')
def step_impl(context, text):
    context.page_object.click_on_link(HIDDEN_OPTIONS_BUTTON)
    context.page_object.search_for(text)

@then(u'I must see the page title "{title}"')
def step_impl(context, title):
    assert_that(context.page_object.get_page_title(), equal_to(title))

@then(u'I must see the header with css class "{css_class}" and with title "{title}"')
def step_impl(context, css_class, title):
    assert_that(context.page_object.get_header(css_class), equal_to(title))
