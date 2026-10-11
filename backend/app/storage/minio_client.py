from functools import lru_cache
from minio import Minio
from app.config import settings

@lru_cache(maxsize=1)
def client() -> Minio:
    c = Minio(
        settings.MINIO_ENDPOINT,
        access_key=settings.MINIO_ACCESS_KEY,
        secret_key=settings.MINIO_SECRET_KEY,
        secure=settings.MINIO_SECURE,
    )
    if not c.bucket_exists(settings.MINIO_BUCKET):
        c.make_bucket(settings.MINIO_BUCKET)
    return c

def upload(key: str, data: bytes, content_type: str = "application/octet-stream"):
    from io import BytesIO
    c = client()
    c.put_object(settings.MINIO_BUCKET, key, BytesIO(data), len(data),
                 content_type=content_type)

def download(key: str) -> bytes:
    c = client()
    resp = c.get_object(settings.MINIO_BUCKET, key)
    try:
        return resp.read()
    finally:
        resp.close()
        resp.release_conn()
