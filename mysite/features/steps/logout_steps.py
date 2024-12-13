from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "http://127.0.0.1:8000"  # Sesuaikan dengan URL server lokal Anda

@given('the user is logged into the dashboard')
def step_user_logged_in(context):
    # Inisialisasi WebDriver
    context.driver = webdriver.Chrome()  # Pastikan WebDriver telah diinstal
    context.driver.maximize_window()

    # Simulasikan login
    context.driver.get(f"{BASE_URL}/")
    context.driver.find_element(By.NAME, "email").send_keys("dimasrespati@gmail.com")  # Sesuaikan username
    context.driver.find_element(By.NAME, "password").send_keys("andika23")  # Sesuaikan password
    login_button = context.driver.find_element(By.XPATH, "//button[text()='Sign In']")
    login_button.click()

    # Pastikan pengguna berhasil masuk ke dashboard
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "logout"))
    )


@when('the user clicks the "Logout" button')
def step_click_logout(context):
    logout_button = context.driver.find_element(By.LINK_TEXT, "Logout")
    logout_button.click()


@then('the user is redirected to the login page')
def step_redirected_to_login(context):
    WebDriverWait(context.driver, 10).until(
        EC.url_contains(f"{BASE_URL}/")
    )
    assert "Login" in context.driver.title, "User is not redirected to the login page."


@then('a success message is displayed')
def step_verify_success_message(context):
    success_message = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "messages"))
    )
    assert "You have been logged out successfully." in success_message.text, "Success message is not displayed."

    context.driver.quit()
