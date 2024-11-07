from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
chrome_options.add_argument("--disable-gpu")  # Applicable to Windows environments
chrome_options.add_argument("--window-size=1280x1024")  # Set a specific window size

# Initialize the Chrome WebDriver with these options
driver = webdriver.Chrome(options=chrome_options)

# Initialize a test case result list
test_results = []

# Function to open a page
def open_page(url):
    try:
        driver.get(url)
        print(f"Opened page: {url}")
        test_results.append({"test": "open_page", "result": "Passed"})
    except Exception as e:
        test_results.append({"test": "open_page", "result": "Failed", "error": str(e)})

# Function to perform a Google search (Simulated failure)
def search_in_google(query):
    try:
        # Simulating a failure by looking for an incorrect element name
        search_box = driver.find_element(By.NAME, "non_existent_name")
        search_box.send_keys(query + Keys.RETURN)
        print(f"Searching for: {query}")
        time.sleep(2)  # Allow time for the results to load
        test_results.append({"test": "search_in_google", "result": "Passed"})
    except Exception as e:
        test_results.append({"test": "search_in_google", "result": "Failed", "error": str(e)})

# Function to extract search result (Simulated success)
def extract_search_results():
    try:
        results = driver.find_elements(By.CSS_SELECTOR, 'h3')
        if not results:
            raise Exception("No results found")
        
        for result in results:
            title = result.text
            link = result.find_element(By.XPATH, '..').get_attribute('href')
            print(f"Title: {title}, Link: {link}")
        
        test_results.append({"test": "extract_search_results", "result": "Passed"})
    except Exception as e:
        test_results.append({"test": "extract_search_results", "result": "Failed", "error": str(e)})

# Function to take a screenshot (Simulated success)
def take_screenshot(file_name):
    try:
        driver.save_screenshot(file_name)
        print(f"Screenshot saved as: {file_name}")
        test_results.append({"test": "take_screenshot", "result": "Passed"})
    except Exception as e:
        test_results.append({"test": "take_screenshot", "result": "Failed", "error": str(e)})

# Function to close the browser (Simulated success)
def close_browser():
    try:
        driver.quit()
        print("Browser closed.")
        test_results.append({"test": "close_browser", "result": "Passed"})
    except Exception as e:
        test_results.append({"test": "close_browser", "result": "Failed", "error": str(e)})

# Function to print the final test report
def print_test_report():
    print("\nTest Report:")
    for result in test_results:
        print(f"Test: {result['test']} - Result: {result['result']}")
        if "error" in result:
            print(f"  Error: {result['error']}")

# Example
if __name__ == "__main__":
    open_page("https://www.google.com")  # This should pass
    search_in_google("Selenium WebDriver")  # This will fail
    extract_search_results()  # This should pass
    take_screenshot("screenshot.png")  # This should pass
    close_browser()  # This should pass
    print_test_report()
