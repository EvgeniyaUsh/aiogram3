# -*- coding: utf-8 -*-

import logging

import boto3

from settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, BUCKET_NAME, REGION_NAME


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
    )  # Создаем клиент для работы с S3
    return s3_client


# Функция для загрузки файла в S3
def upload_to_s3(file_path, object_name):
    s3_client = get_s3_client()
    try:
        # Загрузка файла в S3
        s3_client.upload_fileobj(file_path, BUCKET_NAME, object_name)
        print(f"Файл {object_name} успешно загружен в S3!")
    except Exception as e:
        print(f"Ошибка при загрузке файла: {e}")
