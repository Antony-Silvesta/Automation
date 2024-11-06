import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Fixture to set up and tear down the WebDriver
@pytest.fixture
def driver():
    # Set Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Enable headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Set up Chrome driver with options
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    yield driver  # Provide the fixture value and run the test
    
    # Quit the driver after the test completes
    driver.quit()

# Test function using the driver fixture
def test_google_search(driver):
    # Open Google
    driver.get("https://www.google.com")

    # Wait for the search box to be visible
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "q")))

    # Search for a term
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium Python")
    search_box.submit()

    # Wait for the title to contain the search term
    WebDriverWait(driver, 10).until(EC.title_contains("Selenium Python"))

    # Verify if the title contains "Selenium Python"
    assert "Selenium Python" in driver.title
    print("Google Search Test Passed.")
