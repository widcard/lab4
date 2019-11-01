"""
lab4: Q1h: get information from Security group
QA
"""
import boto3
from botocore.exceptions import ClientError
ec2 = boto3.client('ec2')
try:
    response = ec2.describe_security_groups(GroupIds=['sg-0678af5450af04d37'])
    print('success',response)
except ClientError as e:
    print(e)