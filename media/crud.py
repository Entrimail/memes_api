from minio import Minio
from config import settings


BUCKET_NAME = settings.bucket_name


def upload_image(file):
    client = Minio(
        endpoint=settings.endpoint,
        access_key=settings.access_key,
        secret_key=settings.secret_key,
        secure=False,
    )

    destination_file = file.filename

    found = client.bucket_exists(BUCKET_NAME)
    if not found:
        client.make_bucket(BUCKET_NAME)
        print("Created bucket", BUCKET_NAME)
    else:
        print("Bucket", BUCKET_NAME, "already exists")

    client.put_object(BUCKET_NAME, destination_file, file.file, file.size)
    print(
        file.filename,
        "successfully uploaded as object",
        destination_file,
        "to bucket",
        BUCKET_NAME,
    )
    url = client.get_presigned_url(
        method="GET", bucket_name=BUCKET_NAME, object_name=file.filename
    )
    return url
