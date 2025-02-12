# Appium Mobile Setup
@pytest.fixture(scope="function")
def mobile_browser():
    desired_caps = {
        "platformName": Config.MOBILE_PLATFORM,
        "deviceName": Config.MOBILE_DEVICE_NAME,
        "app": Config.MOBILE_APP,
        "automationName": "UiAutomator2"
    }
    driver = mobile_webdriver.Remote(Config.GRID_URL, desired_caps)
    yield driver
    driver.quit()
