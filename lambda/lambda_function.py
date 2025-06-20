import json
import base64
import boto3

runtime = boto3.client('sagemaker-runtime')
bedrock = boto3.client('bedrock-runtime')

def lambda_handler(event, context):
    body = json.loads(event["body"])
    img_data = base64.b64decode(body["image_base64"])

    response = runtime.invoke_endpoint(
        EndpointName="grape-disease-endpoint",
        ContentType='application/x-image',
        Body=img_data
    )

    prediction = int(response['Body'].read().decode())
    classes = ["Black_rot", "Esca", "Healthy", "Leaf_blight"]
    disease = classes[prediction]

    prompt = f"Explain {disease} disease in grape crops and provide actionable treatment steps."

    bedrock_resp = bedrock.invoke_model(
        modelId="anthropic.claude-v2",
        body=json.dumps({"prompt": prompt, "max_tokens": 300}),
        accept="application/json",
        contentType="application/json"
    )

    explanation = json.loads(bedrock_resp['body'].read())["completion"]

    return {
        "statusCode": 200,
        "body": json.dumps({"disease": disease, "explanation": explanation})
    }
