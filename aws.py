import boto3
import os


def convert_file_path_s3(file_path):
    file_path = file_path.replace(os.sep, '/')
    return file_path


def upload_file(file, bucket, file_name=None):
    file = convert_file_path_s3(file)
    s3 = boto3.resource('s3')
    if not file_name:
        file_name = os.path.split(file)[1]
    file_name = convert_file_path_s3(file_name)
    s3.meta.client.upload_file(file, bucket, file_name)
