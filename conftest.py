import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Set up the Chrome WebDriver for all tests
@pytest.fixture(scope='module')
def driver():
    # Configure Chrome options for headless mode and other settings
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
    chrome_options.add_argument("--disable-gpu")  # Applicable to Windows environments
    chrome_options.add_argument("--window-size=1280x1024")  # Set a specific window size

    # Initialize WebDriver using ChromeDriverManager
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    
    # Yield the driver to the tests
    yield driver
    
    # Teardown: Quit the driver after all tests in the module are done
    driver.quit()
