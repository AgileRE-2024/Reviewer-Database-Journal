from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@given('Saya berada di halaman login')
def step_given_berada_di_halaman_login(context):
    context.browser = webdriver.Chrome()  # Ganti dengan driver sesuai setup Anda
    context.browser.get('http://127.0.0.1:8000/')  # URL halaman login

@when('Saya mengisi kolom "{field}" dan "{field2}" dengan benar')
def step_when_mengisi_kredensial_benar(context, field, field2):
    context.browser.find_element(By.NAME, 'email').send_keys('dimasrespati@gmail.com')  # Ganti dengan username benar
    context.browser.find_element(By.NAME, 'password').send_keys('andika23')  # Ganti dengan password benar

@when('Saya mengisi kolom "{field}" dan/atau "{field2}" dengan salah')
def step_when_mengisi_kredensial_salah(context, field, field2):
    context.browser.find_element(By.NAME, 'email').send_keys('wronguser@gmail.com')
    context.browser.find_element(By.NAME, 'password').send_keys('wrongpass')

@when(u'Saya klik tombol "Sign In"')
def step_impl(context):
    # Cari tombol berdasarkan teks atau atributnya
    login_button = context.browser.find_element(By.XPATH, "//button[text()='Sign In']")
    login_button.click()

@then(u'Saya melihat pop-up "Invalid email or password"')
def step_impl(context):
    # Tunggu hingga pesan error muncul dalam elemen dengan class 'alert'
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    # Tunggu pesan error muncul
    message_element = WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'alert'))
    )

    # Verifikasi apakah pesan error berisi teks yang diharapkan
    assert "Invalid email or password" in message_element.text, \
        f"Expected error message not found. Found: {message_element.text}"


@when(u'Saya dialihkan ke dashboard')
def step_impl(context):
    # Tunggu hingga URL dialihkan ke dashboard
    time.sleep(2)  # Tambahkan waktu tunggu opsional
    expected_url = 'http://127.0.0.1:8000/dashboard/'  # Sesuaikan dengan URL dashboard Anda
    assert context.browser.current_url == expected_url, \
        f"Expected to be on dashboard, but was on {context.browser.current_url}"

@then(u'Saya tetap berada di halaman login')
def step_impl(context):
    # Verifikasi URL halaman login
    expected_url = 'http://127.0.0.1:8000/'  # Sesuaikan dengan URL halaman login Anda
    assert context.browser.current_url == expected_url, \
        f"Expected to remain on login page, but was on {context.browser.current_url}"