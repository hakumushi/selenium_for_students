from pages.HomePage import HomePage
from hamcrest import assert_that, equal_to

home_menu_item = "HOME"
selenium_menu_item = "SELENIUM"

@given(u'I am on Home Page')
def step_impl(context):
    context.page_object = HomePage(context.driver)
    context.page_object.open_url()

@when(u'I open the home screen')
def step_impl(context):
    context.page_object.click_on_menu_item(home_menu_item)

@when(u'I click on sub menu item "{sub_menu_item}"')
def step_impl(context, sub_menu_item):
    context.page_object.click_on_menu_item(selenium_menu_item)
    context.page_object.click_on_submenu_item(sub_menu_item)

@when(u'I search for "{text}"')
def step_impl(context, text):
    context.page_object.open_hidden_options()
    context.page_object.search_for(text)

@then(u'I must see the page title "{title}"')
def step_impl(context, title):
    assert_that(context.page_object.get_page_title(), equal_to(title))

@then(u'I must see the header with css class "{css_class}" and with title "{title}"')
def step_impl(context, css_class, title):
    assert_that(context.page_object.get_header(css_class), equal_to(title))
