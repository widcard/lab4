"""
lab4: Q1i:delect security group
QA
"""
import boto3
from botocore.exceptions import ClientError
ec2 = boto3.client('ec2')
try:
    response = ec2.delete_security_group(GroupName='lab4_1i')
    print('success',response)
except ClientError as e:
    print(e)