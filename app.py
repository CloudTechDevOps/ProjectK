import linux
import windows dev

def lambda_handler(event, context):
  client = boto3.client('ec2')
  response = client.run_instances(
    ImageId='ami-0614680123427b75e',
    InstanceType='t2.micro',
    KeyName='devops',
    MaxCount=1,
    MinCount=1
)
