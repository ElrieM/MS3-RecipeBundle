import os
from flask import (render_template, request)
from werkzeug.utils import secure_filename
import boto3

if os.path.exists("env.py"):
    import env


s3_bucket_name = os.environ.get("AWS_BUCKET_NAME")
s3_bucket_url = os.environ.get("AWS_DOMAIN")
s3 = boto3.client('s3',
                  aws_access_key_id=os.environ.get('AWS_ACCESS_KEY'),
                  aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY')
                  )


def upload():
    if request.method == 'POST':
        img = request.files['file']
        if img:
            filename = secure_filename(img.filename)
            img.save(filename)
            s3.upload_file(
                Bucket=s3_bucket_name,
                Filename=filename,
                Key=filename
            )
            msg = "Image uploaded successfully! "
    return render_template("recipes/add_recipe.html", msg=msg)
