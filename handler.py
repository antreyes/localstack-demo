import boto3
import os


def entry(event, context):
  clients = {"s3": boto3.client("s3",endpoint_url="http://host.docker.internal:4572",aws_access_key_id="foo",aws_secret_access_key="bar",verify=False,region_name="us-east-1")}
  path = 'images/upload.png'
  png = 'resources/localstack/localstack.png'
  clients["s3"].upload_file(png, os.environ["BUCKET_NAME"], path)
  return {"path": path}

