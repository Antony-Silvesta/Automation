import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Define a fixture for the Selenium WebDriver
@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--no-sandbox")  # Bypass OS security model (useful for CI)
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
    driver = webdriver.Chrome(options=chrome_options)  # Adjust the WebDriver path if necessary
    yield driver
    driver.quit()

def test_login(driver):
    # Open the login page
    driver.get("https://example.com/login")
    
    # Locate the username and password fields and the login button
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")
    
    # Send username and password to the fields
    username_field.send_keys("testuser")
    password_field.send_keys("testpassword")
    
    # Click the login button
    login_button.click()
    
    # Assert that the login was successful by checking if the URL changes or some element appears
    assert "dashboard" in driver.current_url  # Replace with the actual condition for successful login
