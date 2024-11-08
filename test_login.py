import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Define a fixture for the Selenium WebDriver with headless mode enabled
@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--no-sandbox")  # Required for some environments
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
    chrome_options.add_argument("--window-size=1920,1080")  # Set screen size for consistent behavior

    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

def test_example(driver):
    driver.get("https://example.com")
    assert "Example Domain" in driver.title
