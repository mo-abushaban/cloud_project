from fastapi.routing import APIRouter
from fastapi import HTTPException, UploadFile
from src.settings import config
from src.services.s3 import s3_client


files_router = APIRouter(prefix="/files")


@files_router.post("/s3")
async def upload_file_to_s3(file: UploadFile):
    try:
        file_contents = await file.read()
        s3_key = f"{file.filename}"  # you can prepend a folder if you want, e.g., "uploads/{file.filename}"

        s3_client.put_object(Bucket=config.S3_BUCKET, Key=s3_key, Body=file_contents)

        file_url = f"{config.S3_ENDPOINT}/{config.S3_BUCKET}/{s3_key}"
        return {"message": "Upload successful", "url": file_url}

    except Exception as e:
        print(f"Failed to upload file: {e}")
        raise HTTPException(status_code=500)
