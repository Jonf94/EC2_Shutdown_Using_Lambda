
import boto3

def lambda_handler(event, context):
    # Create an EC2 client
    ec2_client = boto3.client('ec2')

    # Get all running instances
    response = ec2_client.describe_instances(
        Filters=[
            {
                'Name': 'instance-state-name',
                'Values': ['running']
            }
        ]
    )
    
    # Extract instance IDs
    instance_ids = [
        instance['InstanceId']
        for reservation in response['Reservations']
        for instance in reservation['Instances']
    ]

    # Stop instances if any of them are running
    if instance_ids:
        print(f"Stopping instances: {instance_ids}")
        ec2_client.stop_instances(InstanceIds=instance_ids)
        print("Instances have been stopped successfully.")
    else:
        print('No running instance found.')

    # Return statement
    return {
        'statusCode': 200,
        'body': 'Execution completed'
    }
