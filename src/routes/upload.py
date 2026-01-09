from fastapi.routing import APIRouter
from fastapi import HTTPException, UploadFile
from src.settings import config
from src.services.databricks import databricks_w
from src.services.s3 import s3_client
from fastapi import status, Response

import base64

files_router = APIRouter(prefix="/files")


@files_router.post("/db")
async def run_hello(file: UploadFile):
    contents = await file.read()
    base64_bytes = base64.b64encode(contents)
    base64_string = base64_bytes.decode("utf-8")

    # This will ignore the directory if it already exists
    databricks_w.dbfs.mkdirs(f"{config.UPLOADED_FILES_PATH}/something")

    file_path = f"dbfs:{config.UPLOADED_FILES_PATH}/{file.filename}"

    try:
        databricks_w.dbfs.put(
            path=file_path,
            contents=base64_string,
            overwrite=True,
        )
        return Response(status_code=status.HTTP_201_CREATED)
    except Exception as e:
        print(f"Error uploading file to Databricks DBFS: {e}")
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

@files_router.post("/s3")
async def upload_file_to_s3(file: UploadFile):
    try:
        file_contents = await file.read()
        s3_key = f"{file.filename}"  # you can prepend a folder if you want, e.g., "uploads/{file.filename}"

        s3_client.put_object(
            Bucket=config.S3_BUCKET,
            Key=s3_key,
            Body=file_contents
        )

        file_url = f"{config.S3_ENDPOINT}/{config.S3_BUCKET}/{s3_key}"
        return {"message": "Upload successful", "url": file_url}

    except Exception as e:
        print(f"Failed to upload file: {e}")
        raise HTTPException(status_code=500)
