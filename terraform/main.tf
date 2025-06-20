    provider "aws" {
    region = var.aws_region
    }

    resource "aws_s3_bucket" "grape_model" {
    bucket = var.model_bucket
    force_destroy = true
    }   

    data "aws_iam_policy_document" "sagemaker_trust" {
    statement {
        actions = ["sts:AssumeRole"]
        principals {
        type = "Service"
        identifiers = ["sagemaker.amazonaws.com"]
        }
    }
    }

    resource "aws_iam_role" "sagemaker_exec" {
    name = "sagemaker-exec-role"
    assume_role_policy = data.aws_iam_policy_document.sagemaker_trust.json
    }

    resource "aws_iam_role_policy_attachment" "sagemaker_access" {
    role       = aws_iam_role.sagemaker_exec.name
    policy_arn = "arn:aws:iam::aws:policy/AmazonS3FullAccess"
    }

    data "aws_iam_policy_document" "lambda_trust" {
    statement {
        actions = ["sts:AssumeRole"]
        principals {
        type = "Service"
        identifiers = ["lambda.amazonaws.com"]
        }
    }
    }

    resource "aws_iam_role" "lambda_exec" {
    name = "lambda-exec-role"
    assume_role_policy = data.aws_iam_policy_document.lambda_trust.json
    }

    resource "aws_iam_role_policy_attachment" "lambda_basic_exec" {
    role       = aws_iam_role.lambda_exec.name
    policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
    }

    resource "aws_lambda_function" "grape_api" {
    function_name = "grape-disease-api"
    handler       = "lambda_function.lambda_handler"
    runtime       = "python3.11"
    role          = aws_iam_role.lambda_exec.arn
    filename      = "../lambda/lambda.zip"
    timeout       = 30
    memory_size   = 512
    source_code_hash = filebase64sha256("../lambda/lambda.zip")
    }

    resource "aws_apigatewayv2_api" "grape_api" {
    name          = "grape-disease-api"
    protocol_type = "HTTP"
    }

    resource "aws_apigatewayv2_integration" "grape_integration" {
    api_id             = aws_apigatewayv2_api.grape_api.id
    integration_type   = "AWS_PROXY"
    integration_uri    = aws_lambda_function.grape_api.invoke_arn
    integration_method = "POST"
    payload_format_version = "2.0"
    }

    resource "aws_apigatewayv2_route" "grape_route" {
    api_id    = aws_apigatewayv2_api.grape_api.id
    route_key = "POST /predict"
    target    = "integrations/${aws_apigatewayv2_integration.grape_integration.id}"
    }

    resource "aws_apigatewayv2_stage" "default_stage" {
    api_id      = aws_apigatewayv2_api.grape_api.id
    name        = "$default"
    auto_deploy = true
    }

    resource "aws_lambda_permission" "allow_apigw" {
    statement_id  = "AllowExecutionFromAPIGateway"
    action        = "lambda:InvokeFunction"
    function_name = aws_lambda_function.grape_api.function_name
    principal     = "apigateway.amazonaws.com"
    source_arn    = "${aws_apigatewayv2_api.grape_api.execution_arn}/*/*"
    }
