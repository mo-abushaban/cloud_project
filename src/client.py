from fastapi import FastAPI, UploadFile
from databricks.sdk import WorkspaceClient
from src.settings import config

w = WorkspaceClient(
  host  = config.DATABRICKS_HOST,
  token = config.DATABRICKS_TOKEN.get_secret_value(),
)

for c in w.clusters.list():
  print(c.cluster_name)

app = FastAPI()

@app.post("/run/hello")
async def run_hello(file: UploadFile):
    input_path = "dbfs:/cloud-spark/input/data.csv"
    output_path = "dbfs:/cloud-spark/output/hello"

    run = db.submit_job(
        python_file="dbfs:/cloud-spark/jobs/hello.py",
        args=[input_path, output_path]
    )

    return {"run_id": run["run_id"]}
