import pytest
import os

# Hook for adding additional information in the HTML report
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    report = outcome.get_result()

    # Check if the test failed at the 'call' phase
    if report.when == 'call' and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            # Ensure screenshots directory exists
            screenshot_path = f"screenshots/{item.name}.png"
            os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)

            # Save the screenshot
            if driver.save_screenshot(screenshot_path):
                print(f"Screenshot saved at: {screenshot_path}")
            else:
                print("Failed to save screenshot.")

            # Attach screenshot to HTML report if the plugin is available
            pytest_html = item.config.pluginmanager.getplugin('html')
            if pytest_html:
                extra = getattr(report, 'extra', [])
                extra.append(pytest_html.extras.image(screenshot_path))
                report.extra = extra
            else:
                print("HTML plugin is not available.")
