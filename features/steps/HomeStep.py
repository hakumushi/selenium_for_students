from pages.HomePage import HomePage
from hamcrest import assert_that, equal_to

#happy example =)
@given(u'I am on Home Page')
def step_impl(context):
    context.page_object = HomePage(context.driver)
    context.page_object.open_url()

@when(u'I open the home screen')
def step_impl(context):
    context.page_object.link_click("HOME")

@then(u'I must see the page title "{title}"')
def step_impl(context, title):
    assert_that(context.page_object.get_page_title(), equal_to(title))
