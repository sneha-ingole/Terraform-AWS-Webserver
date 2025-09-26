# Terraform Lambda API Gateway

This project provisions an **AWS Lambda function** and exposes it through **API Gateway** using Terraform.  
It demonstrates how to deploy a serverless function and make it accessible via an HTTP endpoint.

---

## 🚀 Features
- Creates an AWS Lambda function
- Configures an API Gateway REST API
- Integrates Lambda with API Gateway
- Outputs the public **Invoke URL** of the API

---

## 📂 Project Structure

terraform-lambda-apigateway/

│-- main.tf

│-- variables.tf

│-- outputs.tf

│-- provider.tf

│-- lambda_function.py

│-- README.md


---

## ⚡ Prerequisites
- [Terraform](https://developer.hashicorp.com/terraform/downloads) installed
- AWS account with IAM credentials
- AWS CLI configured (`aws configure`)
- Basic knowledge of AWS Lambda & API Gateway

---

## 🔧 Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/sneha-ingole/terraform-lambda-apigateway.git
   cd terraform-lambda-apigateway

2.Initialize Terraform:

terraform init

3.Plan the deployment:

terraform plan

4.Apply configuration:

terraform apply -auto-approve

5.After successful deployment, Terraform will output the API Gateway Invoke URL.
You can test it with:

curl https://08982f1c5bf93d976.execute-api.us-east-1.amazonaws.com/dev/

🐍 Sample Lambda Function (lambda_function.py)

import json

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello from Lambda + API Gateway!",
            "input": event
        }),
    }
This simple function returns a JSON response when invoked via API Gateway.

🧹 Clean Up

To destroy all resources:

terraform destroy -auto-approve

📜 License

This project is licensed under the MIT License.

---




