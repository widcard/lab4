"""
lab4: Q1f: Create a new key pair
QA
"""
import boto3
ec2 = boto3.client('ec2')
response = ec2.create_key_pair(KeyName='cyu004Lab4fkey')
print('success',response)
                               