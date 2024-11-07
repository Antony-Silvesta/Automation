import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# Set up Chrome options
@pytest.fixture(scope='module')
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
    chrome_options.add_argument("--disable-gpu")  # Applicable to Windows environments
    chrome_options.add_argument("--window-size=1280x1024")  # Set a specific window size

    driver = webdriver.Chrome(options=chrome_options)
    yield driver  # Use this driver for tests
    driver.quit()  # Ensure that the browser is closed after tests

# Function to open a page
def test_open_page(driver):
    driver.get("https://www.google.com")
    assert driver.title == "Google", "Failed to open Google page"

# Function to perform a Google search (Simulated failure)
def test_search_in_google(driver):
    try:
        search_box = driver.find_element(By.NAME, "q")  # Corrected to the actual search input element
        search_box.send_keys("Selenium WebDriver" + Keys.RETURN)
        time.sleep(2)  # Allow time for the results to load
        assert "Selenium WebDriver" in driver.page_source, "Search result not found"
    except Exception as e:
        pytest.fail(f"Google search failed: {str(e)}")

# Function to extract search results (Simulated success)
def test_extract_search_results(driver):
    try:
        results = driver.find_elements(By.CSS_SELECTOR, 'h3')
        assert len(results) > 0, "No results found"
        
        for result in results:
            title = result.text
            link = result.find_element(By.XPATH, '..').get_attribute('href')
            print(f"Title: {title}, Link: {link}")
    except Exception as e:
        pytest.fail(f"Extract search results failed: {str(e)}")

# Function to take a screenshot (Simulated success)
def test_take_screenshot(driver):
    try:
        driver.save_screenshot("screenshot.png")
        assert True, "Screenshot saved successfully"
    except Exception as e:
        pytest.fail(f"Screenshot capture failed: {str(e)}")

# Group tests into a class 
@pytest.mark.usefixtures("driver")
class TestGoogleAutomation:

    def test_open_page(self, driver):
        test_open_page(driver)

    def test_search_in_google(self, driver):
        test_search_in_google(driver)

    def test_extract_search_results(self, driver):
        test_extract_search_results(driver)

    def test_take_screenshot(self, driver):
        test_take_screenshot(driver)
