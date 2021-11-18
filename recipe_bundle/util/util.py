import os
from flask import (render_template, request)
from werkzeug.utils import secure_filename
import boto3
from botocore.exceptions import ClientError
import logging
from typing import Tuple

if os.path.exists("env.py"):
    import env


# AWS variables
s3_bucket_name = os.environ.get("AWS_BUCKET_NAME")
s3_bucket_url = os.environ.get("AWS_DOMAIN")
s3 = boto3.client('s3',
                  aws_access_key_id=os.environ.get('AWS_ACCESS_KEY'),
                  aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY')
                  )


# Adapted from https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-uploading-files.html
def upload_img(file_name, object_name=None):
    """
    Upload a file to recipes S3 bucket
    :param file_name: File to be uploaded
    :param bucket: Bucket to which uploading
    :param object_name: S3 object name - if not specified, uses file_name
    :returns: If successfully uploaded returns True, else False
    """
    img = request.files[file_name]
    img_file = secure_filename(img.filename)
    # If S3 object_name not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload file to S3 bucket
    try:
        s3_client = boto3.client('s3')
        s3_client.Bucket('s3_bucket_name').put_object(Key=img_file, Body=img)
    except ClientError:
        raise Exception("An error occurred when uploading the image")

    img_url = s3_bucket_url + img_file
    return img_url
