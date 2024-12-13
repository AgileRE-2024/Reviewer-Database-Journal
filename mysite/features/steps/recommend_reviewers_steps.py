from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
from selenium.webdriver.common.alert import Alert

@given("the user is on the upload manuscript page")
def step_open_upload_page(context):
    context.driver = webdriver.Chrome()  # Pastikan WebDriver diatur dengan benar
    context.driver.get("http://127.0.0.1:8000/upload/detail/")  # Ganti dengan URL lokal Anda
    context.driver.maximize_window()

@when("the user fills the form with valid data")
def step_fill_form(context):
    title_input = context.driver.find_element(By.ID, "journal-title")
    abstract_input = context.driver.find_element(By.ID, "abstract")
    
    title_input.send_keys("Sample Paper Title")
    abstract_input.send_keys("This is a sample abstract for testing purposes.")

@when("the user agrees to the terms and conditions")
def step_agree_terms(context):
    terms_checkbox = context.driver.find_element(By.ID, "terms")
    ActionChains(context.driver).move_to_element(terms_checkbox).click().perform()

@when("the user submits the form")
def step_submit_form(context):
    submit_button = context.driver.find_element(By.CLASS_NAME, "submit-btn")
    submit_button.click()

@then("the user is redirected to the recommendation page")
def step_redirect_check(context):
    WebDriverWait(context.driver, 10).until(
        EC.url_contains("/recommendation/")
    )
    assert "/recommendation/" in context.driver.current_url

@then("the system displays reviewer recommendations")
def step_check_recommendations(context):
    recommendations = json.loads(context.driver.execute_script("return sessionStorage.getItem('recommendations')"))
    assert len(recommendations) > 0, "No recommendations found"
    for recommendation in recommendations:
        assert "name" in recommendation
        assert "highest_score" in recommendation
    
    context.driver.quit()

@when('the user leaves the "journal-title" field empty')
def step_leave_title_empty(context):
    title_input = context.driver.find_element(By.ID, "journal-title")
    title_input.clear()  # Kosongkan inputan title

@when('the user fills the "abstract" field with valid data')
def step_fill_abstract(context):
    abstract_input = context.driver.find_element(By.ID, "abstract")
    abstract_input.send_keys("This is a sample abstract for testing purposes.")

import time

@then('a JavaScript alert appears with the message "Please fill out this field"')
def step_check_validation_message(context):
    title_input = context.driver.find_element(By.ID, "journal-title")
    context.driver.execute_script("arguments[0].focus();", title_input)

    submit_button = context.driver.find_element(By.CLASS_NAME, "submit-btn")
    submit_button.click()

    # Tunggu untuk memastikan validasi diproses
    time.sleep(2)

    validation_message = title_input.get_attribute("validationMessage")
    expected_message = "Please fill out this field."

    assert validation_message == expected_message, f"Unexpected validation message: {validation_message}"

