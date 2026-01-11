from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.settings import config

from src.services.emr import emr_client


tasks_router = APIRouter(prefix="/tasks")


class SparkJobRequest(BaseModel):
    s3_script_path: str
    num_executors: int = 4
    executor_cores: int = 4
    job_name: str = "Spark Job from FastAPI"


@tasks_router.post("/")
async def run_spark_on_emr(job: SparkJobRequest):
    """
    Make sure that you have already uploaded your Spark script to S3
    Make sure that you setup AWS EMR
    """
    try:
        args = [
            "spark-submit",
            "--deploy-mode",
            "cluster",
            "--num-executors",
            str(job.num_executors),
            "--executor-cores",
            str(job.executor_cores),
            "--conf",
            "spark.dynamicAllocation.enabled=false",
            job.s3_script_path,
        ]

        step = {
            "Name": job.job_name,
            "ActionOnFailure": "CONTINUE",
            "HadoopJarStep": {"Jar": "command-runner.jar", "Args": args},
        }

        response = emr_client.add_job_flow_steps(
            JobFlowId=config.EMR_CLUSTER_ID, Steps=[step]
        )

        step_id = response["StepIds"][0]
        return {"message": "Spark job submitted", "step_id": step_id}

    except Exception as e:
        print(f"Failed to submit Spark job: {e}")
        raise HTTPException(status_code=500)
