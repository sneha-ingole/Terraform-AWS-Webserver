output "lambda_function_name" {
  value = aws_lambda_function.example.function_name
}

output "api_endpoint" {
  value = aws_apigatewayv2_api.api.api_endpoint
}
