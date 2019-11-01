"""
lab4: Q1f: delete a key pair
QA
"""
import boto3
ec2 = boto3.client('ec2')
response = ec2.delete_key_pair(KeyName='cyu004Lab4fkey')
print('success',response)
                               