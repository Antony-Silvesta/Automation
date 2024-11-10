import pytest
from selenium.webdriver.common.by import By

# Test 7: This will be rerun - using pytest-rerunfailures
@pytest.mark.retry(tries=3, delay=2)  # Retry the test 3 times with a 2-second delay
def test_rerun(driver):
    driver.get("https://www.wikipedia.org/")
    search_input = driver.find_element(By.ID, "searchInput")
    assert search_input is None  # This will fail initially, triggering reruns
