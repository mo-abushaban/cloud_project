from databricks.sdk import WorkspaceClient
from src.settings import config

databricks_w = WorkspaceClient(
  host  = config.DATABRICKS_HOST,
  token = config.DATABRICKS_TOKEN.get_secret_value(),
)

for c in databricks_w.clusters.list():
  print(c.cluster_name)
