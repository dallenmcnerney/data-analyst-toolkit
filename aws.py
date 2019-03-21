import boto3
import os


def upload_file(file, bucket, filename=None):
    s3 = boto3.resource('s3')
    if not filename:
        filename = os.path.split(file)[1]
    s3.meta.client.upload_file(file, bucket, filename)

