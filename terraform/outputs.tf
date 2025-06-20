output "api_gateway_url" {
  value = aws_apigatewayv2_api.grape_api.api_endpoint
}

output "lambda_function_name" {
  value = aws_lambda_function.grape_api.function_name
}

output "s3_bucket_name" {
  value = aws_s3_bucket.grape_model.bucket
}

output "sagemaker_role_arn" {
  value = aws_iam_role.sagemaker_exec.arn
}
