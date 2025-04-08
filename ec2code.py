import boto3

# Create EC2 client
ec2 = boto3.resource('ec2', region_name='ap-south-1')  # Change region as needed

# Launch instance
instance = ec2.create_instances(
    ImageId='ami-0c768662cc797cd75',   # Replace with your AMI ID
    InstanceType='t2.micro',           # Instance type
    MinCount=1,
    MaxCount=1,
    KeyName='Singapore.pem',      # Replace with your key pair name
    SecurityGroupIds=['sg-xxxxxxxx'],  # Replace with your security group ID
    SubnetId='subnet-xxxxxxxx',        # Replace with your subnet ID
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [{'Key': 'Name', 'Value': 'MyEC2Instance'}]
        }
    ]
)

print(f"EC2 Instance ID: {instance[0].id}")

