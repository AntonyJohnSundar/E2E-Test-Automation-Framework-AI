# WebDriver Setup
@pytest.fixture(scope="function")
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    driver.get(Config.BASE_URL)
    yield driver
    driver.quit()

# Playwright Setup
@pytest.fixture(scope="function")
def playwright_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(Config.BASE_URL)
        yield page
        browser.close()
