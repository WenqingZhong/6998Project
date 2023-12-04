import boto3
import time

def upload_file_to_s3(file_name, bucket, object_name=None):
    """
    Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        start_time = time.time()
        s3_client.upload_file(file_name, bucket, object_name)
        end_time = time.time()
        return end_time - start_time
    except Exception as e:
        print(e)
        return None

# Example usage
file_name = '100.txt'  # Replace with your file name
bucket_name = '6998s3'  # Replace with your bucket name

latency = upload_file_to_s3(file_name, bucket_name)
if latency is not None:
    print(f"Upload latency: {latency} seconds")
else:
    print("Failed to upload file.")
