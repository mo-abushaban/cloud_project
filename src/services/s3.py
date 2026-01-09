import boto3
from botocore.client import Config
from src.settings import config

s3_client = boto3.client(
    "s3",
    endpoint_url=config.S3_ENDPOINT,
    aws_access_key_id=config.AWS_ACCESS_KEY,
    aws_secret_access_key=config.AWS_SECRET_KEY.get_secret_value(),
    region_name=config.AWS_REGION,
    config=Config(signature_version="s3v4", s3={"addressing_style": "path"}),
)
