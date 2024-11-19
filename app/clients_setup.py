import logging

import boto3

from settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, REGION_NAME


def get_rekognition_client():
    """Настройка для подключения к boto3.

    Returns:
        boto3_client (object): client для amazon rekognition.
    """
    logging.info("Create rekognition client.")
    boto3_client = boto3.client(
        "rekognition",
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=REGION_NAME,
    )
    return boto3_client


def get_s3_client():
    """Настройка для подключения к boto3.

    Returns:
        s3_client (object): client для s3 хранилища.
    """
    logging.info("Create s3 client.")
    s3_client = boto3.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )
    return s3_client
