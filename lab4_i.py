"""
lab4: Q1i:create a new security group
QA
"""
import boto3
from botocore.exceptions import ClientError
ec2 = boto3.client('ec2')
try:
    response = ec2.create_security_group(GroupName='lab4_1i',
                                        Description ='lab4_1i crated 10/29/19')
    print('success',response)
except ClientError as e:
    print(e)