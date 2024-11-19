import logging

from app.clients_setup import get_s3_client
from settings import BUCKET_NAME


def upload_to_s3(file_path, object_name):
    """Загрузка фото в s3 бакет.

    Args:
        file_path (str): Путь к файлу.
        object_name (str): Название файла.
    """
    s3_client = get_s3_client()
    try:
        s3_client.upload_fileobj(file_path, BUCKET_NAME, object_name)
        print(f"Файл {object_name} загружен в S3!")
    except Exception as e:
        print(f"Ошибка при загрузке файла: {e}")
