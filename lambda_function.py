import boto3

sm = boto3.client("sagemaker")
PIPELINE_NAME = "DiseaseClassificationPipeline"

def lambda_handler(event, context):
    bucket = event["detail"]["bucket"]["name"]
    key = event["detail"]["object"]["key"]
    s3_uri = f"s3://{bucket}/{key}"

    response = sm.start_pipeline_execution(
        PipelineName=PIPELINE_NAME,
        PipelineParameters=[
            {"Name": "ProcessingInstanceCount", "Value":str(1)},
            {"Name": "TrainingInstanceType", "Value": "ml.m5.xlarge"},
            {"Name": "ModelApprovalStatus", "Value": "PendingManualApproval"},
            {"Name": "InputData", "Value": "s3://disease-classification-12052025/pipeline/input-data-update/Training.csv"},
            {"Name": "TestData", "Value": "s3://disease-classification-12052025/pipeline/input-data-update/Testing.csv"},
            {"Name": "BatchData", "Value": "s3://disease-classification-12052025/pipeline/test_no_target.csv"},
            {"Name": "AccThreshold", "Value": str(0.97)}
        ]
    )

    return {
        "pipelineExecutionArn": response["PipelineExecutionArn"]
    }

