from pages.HomePage import HomePage
from hamcrest import assert_that, equal_to

@given(u'I am on Home Page')
def step_impl(context):
    context.page_object = HomePage(context.driver)
    context.page_object.open_url()

@when(u'I open the home screen')
def step_impl(context):
    context.page_object.click_on_home_screen_link()

@when(u'I click on sub menu item Curso Selenium')
def step_impl(context):
    context.page_object.click_on_selenium_link()
    context.page_object.click_on_curso_selenium_link()

@when(u'I click on sub menu item Formulario Simples')
def step_impl(context):
    context.page_object.click_on_selenium_link()
    context.page_object.click_on_formulario_link()

@when(u'I search for "{text}"')
def step_impl(context, text):
    context.page_object.open_hidden_options()
    context.page_object.search_for(text)

@then(u'I must see the page title "{title}"')
def step_impl(context, title):
    assert_that(context.page_object.get_page_title(), equal_to(title))

@then(u'I must see the header with title "{title}"')
def step_impl(context, title):
    real_title = ''
    headers = ['Curso Selenium','Formulário Simples', 'Nada Encontrado']
    if title in headers:
        real_title = context.page_object.get_header_of_a_entry_title()
    elif title == "Resultados da pesquisa por: teste":
        real_title = context.page_object.get_header_of_a_page_title()
    assert_that(real_title, equal_to(title))
