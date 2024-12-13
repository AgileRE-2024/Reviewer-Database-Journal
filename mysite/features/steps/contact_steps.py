from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

BASE_URL = "http://127.0.0.1:8000"  # Sesuaikan dengan URL server lokal Anda

@given('the user is on the Contact page')
def step_open_contact_page(context):
    context.driver = webdriver.Chrome()  # Pastikan WebDriver diatur dengan benar
    context.driver.get(f"{BASE_URL}/contact/")

@then('the user sees a list of contact cards with names, emails, and message buttons')
def step_verify_contact_cards(context):
    contact_cards = context.driver.find_elements(By.CLASS_NAME, "contact-card")
    assert len(contact_cards) > 0, "No contact cards found"

    for card in contact_cards:
        # Periksa nama
        name = card.find_element(By.TAG_NAME, "h3")
        assert name.text, "Name is missing in a contact card"

        # Periksa email
        email = card.find_element(By.TAG_NAME, "p")
        assert email.text, "Email is missing in a contact card"

        # Periksa tombol pesan
        message_btn = card.find_element(By.CLASS_NAME, "message-btn")
        assert message_btn, "Message button is missing in a contact card"

@when('the user clicks the "Message" button for a contact')
def step_click_message_button(context):
    first_message_btn = context.driver.find_element(By.CLASS_NAME, "message-btn")
    context.email_link = first_message_btn.get_attribute("href")
    first_message_btn.click()

@then('the email client opens with the correct email address pre-filled')
def step_verify_email_client(context):
    assert context.email_link.startswith("mailto:"), "Email link does not use the mailto scheme"
    expected_email = context.email_link.split(":")[1]
    assert "@" in expected_email, "Invalid email address in the mailto link"
