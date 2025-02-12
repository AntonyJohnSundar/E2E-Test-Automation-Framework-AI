class Config:
    BASE_URL = "https://example.com"
    BROWSER = "chrome"
    SCREENSHOT_PATH = "reports/screenshots/"
    VIDEO_PATH = "reports/videos/"
    TEST_ENV = "SIT"
    AWS_S3_BUCKET = "your-s3-bucket-name"
    ENABLE_REALTIME_STREAMING = True
    GRID_URL = "http://localhost:4444/wd/hub"
    MOBILE_PLATFORM = "Android"
    MOBILE_DEVICE_NAME = "emulator-5554"
    MOBILE_APP = "path/to/app.apk"