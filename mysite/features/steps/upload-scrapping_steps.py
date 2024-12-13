import os
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "http://127.0.0.1:8000"  # Sesuaikan dengan URL server lokal Anda

@given('the user is on the Upload OJS page')
def step_open_upload_ojs_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get(f"{BASE_URL}/upload/ojs/")

@when('the user selects a valid OJS file and clicks the upload button')
def step_upload_valid_file(context):
    upload_input = context.driver.find_element(By.ID, "ojs-file")
    submit_button = context.driver.find_element(By.ID, "upload-btn")
    
    # Simulasi unggah file dengan file dummy
    test_file_path = os.path.join(os.getcwd(), "test_ojs.xlsx")
    with open(test_file_path, "wb") as f:
        f.write(b"Dummy content for testing.")
    
    upload_input.send_keys(test_file_path)
    submit_button.click()

@then('the file is successfully uploaded')
def step_verify_successful_upload(context):
    WebDriverWait(context.driver, 10).until(
        EC.alert_is_present()
    )
    alert = context.driver.switch_to.alert
    assert "File uploaded successfully!" in alert.text
    alert.accept()

@when('the user clicks the "Start Scraping" button')
def step_click_start_scraping(context):
    start_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "go-btn"))
    )
    start_button.click()

@then('the scraping process starts')
def step_verify_scraping_started(context):
    WebDriverWait(context.driver, 10).until(
        EC.alert_is_present()
    )
    alert = context.driver.switch_to.alert
    assert "Scraping started!" in alert.text
    alert.accept()

@then('scraping statistics are displayed')
def step_verify_scraping_stats(context):
    try:
        # Tunggu alert muncul, jika ada
        WebDriverWait(context.driver, 10).until(EC.alert_is_present())
        alert = context.driver.switch_to.alert
        alert_text = alert.text
        assert "Scraping completed or stopped!" in alert_text, "Unexpected alert message!"
        alert.accept()  # Tutup alert
    except Exception as e:
        print(f"No alert present or error: {e}")

    # Setelah alert ditutup, cari elemen statistik
    stats_element = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "scraping-stats"))
    )
    stats_text = stats_element.text.strip()
    assert stats_text != "", "Scraping statistics are not displayed."

    context.driver.quit()
