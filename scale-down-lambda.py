import boto3
import datetime

# Initialize the EC2 client
ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    # Specify the Auto Scaling Group name
    asg_name = 'your-auto-scaling-group-name'
    
    # Get the current time
    now = datetime.datetime.now()
    print(f"Current time: {now}")

    # Scale down the Auto Scaling Group
    response = ec2.put_scaling_policy(
        PolicyName='ScaleDownPolicy',
        AutoScalingGroupName=asg_name,
        ScalingAdjustment=-1,
        AdjustmentType='ChangeInCapacity'
    )
    
    print("Scale down response:", response)
    return {
        'statusCode': 200,
        'body': 'Scaling down initiated'
    }
