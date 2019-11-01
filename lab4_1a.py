"""
lab4: first Python Boto 3 activity kono Chz da~
QA
"""
import boto3
ec2 = boto3.client('ec2')
response = ec2.describe_instances()
print(response)
