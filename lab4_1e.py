"""
lab4: Q1e: desribe key pair
QA
"""
import sys
import boto3
from botocore.exceptions import ClientError
ec2 = boto3.client('ec2')
response = ec2.describe_key_pairs()
print('success',response)

