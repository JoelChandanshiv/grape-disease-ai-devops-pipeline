import boto3

# Endpoint name (output from deploy.py or Terraform)
endpoint_name = "grape-disease-endpoint-v2"

# Open the test image in binary mode
with open("1f8270ac-8016-457e-8e81-bca5bbcaa784___FAM_B.Msls 1338.JPG", "rb") as image_file:
    image_bytes = image_file.read()

# SageMaker runtime client
client = boto3.client("sagemaker-runtime")

# Invoke the deployed endpoint
response = client.invoke_endpoint(
    EndpointName=endpoint_name,
    ContentType='application/x-image',
    Body=image_bytes
)

# Read and decode prediction result
prediction = int(response["Body"].read().decode())

# Class labels for interpretation
class_mapping = {
    0: "Black Rot",
    1: "Esca (Black Measles)",
    2: "Leaf Blight",
    3: "Healthy"
}

# Output the human-readable result
print("Prediction:", class_mapping.get(prediction, "Unknown Disease"))
