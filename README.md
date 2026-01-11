The AWS role for AWS EMR needs this policy:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "s3:ListAccessPointsForObjectLambda",
                "s3:GetAccessPoint",
                "s3:PutAccountPublicAccessBlock",
                "s3:ListAccessPoints",
                "s3:CreateStorageLensGroup",
                "s3:ListJobs",
                "s3:PutStorageLensConfiguration",
                "s3:ListMultiRegionAccessPoints",
                "s3:ListStorageLensGroups",
                "s3:ListStorageLensConfigurations",
                "s3:ListBucket",
                "s3:GetAccountPublicAccessBlock",
                "s3:ListAllMyBuckets",
                "s3:ListAccessGrantsInstances",
                "s3:PutAccessPointPublicAccessBlock",
                "s3:CreateJob"
            ],
            "Resource": "*"
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": "arn:aws:s3:::*"
        }
    ]
}
```

After the EMR cluster is created, use this setup to run ML on spark:

```bash
spark-submit --deploy-mode cluster --num-executors 4 --executor-cores 4 --conf spark.dynamicAllocation.enabled=false s3://$BUCKET/spark.py

aws emr add-steps \
    --cluster-id j-2AXXXXXXGAPLF \
    --steps Type=CUSTOM_JAR,Name="Run ML",Jar=command-runner.jar,Args=[spark-submit,S3://amzn-s3-demo-bucket/my-app.py]

```

https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-commandrunner.html

