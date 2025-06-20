import sagemaker
from sagemaker.pytorch import PyTorchModel
import os

role = os.environ['SAGEMAKER_ROLE']
sagemaker_session = sagemaker.Session()

model = PyTorchModel(
    model_data='s3://grape-disease-model-bucket/model.tar.gz',  # S3 path to your model
    role=role,
    framework_version='1.13.1',
    py_version='py39',  # ✅ use py39 based on supported versions
    sagemaker_session=sagemaker_session
)

predictor = model.deploy(
    initial_instance_count=1,
    instance_type='ml.m5.large',
    endpoint_name='grape-disease-endpoint-v2'
)

print("✅ Deployed Endpoint:", predictor.endpoint_name)
