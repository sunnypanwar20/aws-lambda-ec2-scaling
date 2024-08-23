# AWS Lambda Functions for EC2 Scaling

This repository contains AWS Lambda functions to scale up and scale down EC2 instances in an Auto Scaling Group.

## Setup

1. **Create IAM Role for Lambda:**
   - Ensure that your Lambda function has the necessary permissions to interact with EC2 Auto Scaling. Create an IAM role with the following policies:
     - `AmazonEC2FullAccess`
     - `AutoScalingFullAccess`
   
2. **Create Lambda Functions:**
   - Create two Lambda functions in the AWS Management Console:
     - **Scale Up Lambda Function**: Use the `scale-up-lambda.py` script.
     - **Scale Down Lambda Function**: Use the `scale-down-lambda.py` script.
   - Attach the IAM role created in step 1 to these Lambda functions.

3. **Configure Lambda Triggers (Optional):**
   - You can set up triggers using Amazon CloudWatch Events to schedule scaling actions. For example, schedule the scale-down function to run during off-peak hours.

4. **Upload the Code:**
   - Navigate to the AWS Lambda console and upload the respective `.py` files as the function code.

## Usage

1. **Deploy Lambda Functions:**
   - Follow the AWS Lambda documentation to deploy the code.

2. **Test the Functions:**
   - Test the functions manually from the Lambda console or configure them to be triggered by events (e.g., CloudWatch Events).

3. **Monitor and Log:**
   - Use Amazon CloudWatch Logs to monitor the execution of these Lambda functions and verify that scaling actions are performed as expected.

## License

This project is licensed under the MIT License.
