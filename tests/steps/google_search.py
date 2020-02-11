from behave import given, when, then
from framework.webapp import webapp
from pages.home import home
import re


@given(u'I visit the website "{website}"')
def step_impl_load_website(context, website):
    webapp.load_website(website)


@when(u'I fill "{value}"')
def step_impl_fill_text(context, value):
    home.fill_find(value)

@then(u'Validate that the search has results')
def step_impl_validate_results(context):
    assert re.search("^Cerca.*resultados.*$", home.text_results())

@then(u'I see this text "{component}"')
def step_impl_verify_component(context, component):
    webapp.verify_component_exists(component)
