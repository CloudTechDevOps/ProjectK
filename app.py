import boto3
client = boto3.client('ec2')
response = client.run_instances(
   ImageId='ami-06b21ccaeff8cd686',
   InstanceType='t2.medium',
   KeyName='eksk8s',
   MaxCount=1,
   MinCount=1
)


