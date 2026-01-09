from fastapi.routing import APIRouter
from fastapi import UploadFile
from src.settings import config
from src.services.databricks import databricks_w
from fastapi import status, Response

import base64

files_router = APIRouter(prefix="/files")


@files_router.post("/")
async def run_hello(file: UploadFile):
    contents = await file.read()
    base64_bytes = base64.b64encode(contents)
    base64_string = base64_bytes.decode("utf-8")

    try:
        databricks_w.dbfs.put(
            path=f"dbfs:{config.UPLOADED_FILES_PATH}/{file.filename}",
            contents=base64_string,
            overwrite=True,
        )
        return Response(status_code=status.HTTP_201_CREATED)
    except Exception as e:
        print(f"Error uploading file to Databricks DBFS: {e}")
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
