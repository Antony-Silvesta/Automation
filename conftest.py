import pytest

# Hook for adding additional information in the HTML report
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    report = outcome.get_result()

    # Check if the test failed at the 'call' phase
    if report.when == 'call' and report.failed:
        # Get the WebDriver instance
        driver = item.funcargs.get("driver")
        if driver:
            # Save the screenshot
            screenshot_path = f"screenshots/{item.name}.png"
            driver.save_screenshot(screenshot_path)

            # Attach screenshot to HTML report
            pytest_html = item.config.pluginmanager.getplugin('html')
            if pytest_html:
                extra = getattr(report, 'extra', [])
                extra.append(pytest_html.extras.image(screenshot_path))
                report.extra = extra

# Fixture to add Selenium browser logs to the report
@pytest.fixture(autouse=True)
def add_selenium_log(request):
    driver = request.node.funcargs.get("driver")
    if driver:
        # Adding browser logs to the report
        for entry in driver.get_log('browser'):
            request.node.user_properties.append(("browser_log", entry))
