# Video Recording
def start_video_capture(test_name):
    if not os.path.exists(Config.VIDEO_PATH):
        os.makedirs(Config.VIDEO_PATH)
    file_path = os.path.join(Config.VIDEO_PATH, f"{test_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.avi")
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(file_path, fourcc, 10.0, (800, 600))
    return out, file_path

def record_frame(out, driver):
    screenshot = driver.get_screenshot_as_png()
    img = cv2.imdecode(np.frombuffer(screenshot, np.uint8), cv2.IMREAD_COLOR)
    img = cv2.resize(img, (800, 600))
    out.write(img)
    if Config.ENABLE_REALTIME_STREAMING:
        threading.Thread(target=stream_frame, args=(img,)).start()

def stop_video_capture(out, file_path):
    out.release()
    logger.info(f"Video recorded: {file_path}")
    upload_to_s3(file_path)