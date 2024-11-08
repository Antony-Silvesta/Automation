import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Define a fixture for the Selenium WebDriver
@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")  # Enable headless mode
    options.add_argument("--disable-gpu")  # Disable GPU acceleration (optional but recommended for headless)
    options.add_argument("--no-sandbox")  # Disable sandboxing (useful in Docker)
    driver = webdriver.Chrome(options=options)  # Pass the options to Chrome
    yield driver
    driver.quit()

def test_example(driver):
    driver.get("https://example.com")
    assert "Example Domain" in driver.title
