from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inisialisasi WebDriver
BASE_URL = "http://127.0.0.1:8000"  # Ganti dengan URL server lokal Anda

@given('the user is on the dashboard page')
def step_open_dashboard(context):
    context.driver = webdriver.Chrome()  # Pastikan WebDriver diatur dengan benar
    context.driver.get(f"{BASE_URL}/dashboard/")

@when('the user clicks the "View All Reviewers" button')
def step_click_view_all_reviewers(context):
    button = context.driver.find_element(By.LINK_TEXT, "View All Reviewers")
    button.click()

@then('the user is redirected to the "All Reviewers" page')
def step_redirected_to_all_reviewers(context):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "table"))
    )
    assert "All Reviewers" in context.driver.title, "Not redirected to the All Reviewers page"

@then('the "All Reviewers" page displays a table of reviewers')
def step_check_reviewers_table(context):
    table = context.driver.find_element(By.TAG_NAME, "table")
    headers = table.find_elements(By.TAG_NAME, "th")
    expected_headers = ["NO", "REVIEWER NAME", "AFFILIATION", "COUNTRY", "EMAIL", "ORCID", "USERNAME", "PAPERS"]
    actual_headers = [header.text for header in headers]
    assert actual_headers == expected_headers, f"Headers do not match. Found: {actual_headers}"

# Tutup WebDriver setelah setiap skenario
def after_scenario(context, scenario):
    context.driver.quit()
