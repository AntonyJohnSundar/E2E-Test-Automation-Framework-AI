# End-to-End Automation Testing Framework - Documentation

## Overview

This framework is designed for automated testing of web and mobile applications. It integrates multiple tools and technologies to support self-healing tests, cloud storage, real-time streaming, video recording, and scalable execution.

## Key Features

- **Cross-Browser Testing:** Selenium & Playwright for seamless automation.
- **Mobile Testing:** Appium support for Android automation.
- **AI Auto-Healing:** Healenium adapts to UI changes.
- **Test Execution:** Pytest for flexible & structured runs.
- **CI/CD Integration:** Jenkins & GitHub Actions compatible.
- **Cloud Storage:** AWS S3 for logs, screenshots & videos.
- **Live Streaming:** Real-time WebRTC/RTMP streaming.
- **Video & Screenshots:** Automated recording & snapshots.
- **Scalability:** Docker & Kubernetes-ready execution.
- **Rich Reporting:** Allure/ExtentReports for analytics.

## Prerequisites

Before setting up the framework, ensure you have the following installed:

- **Python 3.8+**
- **Google Chrome** (for web testing)
- **Node.js** (for Playwright installation)
- **Appium Server** (for mobile testing)
- **Docker** (if running tests in containers)
- **AWS CLI** (if using AWS S3 for cloud storage)
- **Java** (for Selenium Grid execution)

## Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/e2e-test-framework.git
   cd e2e-test-framework
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Install Playwright and browsers:
   ```bash
   playwright install
   ```
4. Configure AWS credentials (if using S3):
   ```bash
   aws configure
   ```
5. Start Appium server (if testing mobile apps):
   ```bash
   appium
   ```

## Folder Structure

```plaintext
e2e_test_framework/
│── config/
│   ├── config.py            # Global configurations
│── drivers/
│   ├── webdriver_setup.py   # WebDriver setup for browsers
│   ├── mobile_setup.py      # Appium setup for mobile
│── utils/
│   ├── logger.py            # Logger configuration
│   ├── video_recorder.py    # Video recording utilities
│   ├── screenshot.py        # Screenshot capture utilities
│   ├── s3_upload.py         # AWS S3 integration
│   ├── streaming.py         # Real-time streaming integration
│── tests/
│   ├── test_amazon_login.py # Amazon login test case
│   ├── test_sample.py       # Example test cases
│── reports/                 # Stores test reports, screenshots, and videos
│── requirements.txt         # Dependencies list
│── pytest.ini               # Pytest configuration
│── run_tests.py             # Main test runner script
```

## Running Tests

Run all tests:

```bash
pytest -v
```

Run specific test cases:

```bash
pytest tests/test_amazon_login.py
```

Generate test reports:

```bash
pytest --alluredir=reports/allure
```

## Configuring the Framework

Modify `config/config.py` to change:

- Base URL
- Browser type
- AWS S3 bucket name
- Enable/Disable streaming
- Mobile device capabilities

## Extending the Framework

To add new test cases:

1. Create a new Python file in `tests/`
2. Use Pytest fixtures for browser setup
3. Implement assertions and validations

To integrate with CI/CD:

- Add a `Jenkinsfile` or GitHub Actions YAML workflow
- Configure Docker/Kubernetes for scalable test execution

## Support & Contribution

For issues and contributions, raise a pull request or report an issue in the repository.

