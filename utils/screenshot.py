# Screenshot capture
def capture_screenshot(driver, test_name):
    if not os.path.exists(Config.SCREENSHOT_PATH):
        os.makedirs(Config.SCREENSHOT_PATH)
    file_path = os.path.join(Config.SCREENSHOT_PATH, f"{test_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
    driver.save_screenshot(file_path)
    logger.info(f"Screenshot saved: {file_path}")
    upload_to_s3(file_path)