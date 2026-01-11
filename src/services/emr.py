import boto3
from src.settings import config


emr_client = boto3.client(
    "emr",
    aws_access_key_id=config.AWS_ACCESS_KEY,
    aws_secret_access_key=config.AWS_SECRET_KEY.get_secret_value(),
    region_name=config.AWS_REGION,
)
