from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@given('I am on the signup page')
def step_given_on_signup_page(context):
    context.browser = webdriver.Chrome()  # Pastikan driver sudah terinstall
    context.browser.get("http://127.0.0.1:8000/signup/")  # Sesuaikan URL proyek Anda

@when('I fill in "{field}" with "{value}"')
def step_when_fill_in_field(context, field, value):
    input_field = context.browser.find_element(By.NAME, field)
    input_field.clear()
    input_field.send_keys(value)

@when('I check the terms and conditions')
def step_when_check_terms(context):
    checkbox = context.browser.find_element(By.ID, 'terms')
    checkbox.click()

@when('I click on "Sign Up"')
def step_when_click_signup(context):
    submit_button = context.browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submit_button.click()

@then('I should see "{message}"')
def step_then_should_see_message(context, message):
    alert = context.browser.find_element(By.CLASS_NAME, 'messages')
    assert message in alert.text
    context.browser.quit()
