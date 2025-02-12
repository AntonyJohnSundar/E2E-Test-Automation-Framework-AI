# AWS S3 Upload
def upload_to_s3(file_path):
    s3 = boto3.client('s3')
    s3.upload_file(file_path, Config.AWS_S3_BUCKET, os.path.basename(file_path))
    logger.info(f"Uploaded {file_path} to S3 bucket {Config.AWS_S3_BUCKET}")
