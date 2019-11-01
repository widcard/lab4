"""
lab4: Q1d: reboot Amazon EC2 instance
QA
"""
import sys
import boto3
from botocore.exceptions import ClientError
ec2 = boto3.client('ec2')

try:
    ec2.reboot_instances(InstanceIds=['i-0a8ca4b5868c96b5b'], DryRun=True)
except ClientError as e:
    if 'DryRunOperation' not in str(e):
            raise
#Dryr run succeeded, run start_instance again without dryrun
try:
    response = ec2.reboot_instances(InstanceIds=['i-0a8ca4b5868c96b5b'], DryRun=False)
    print(response)
except ClientError as e:
                                                                                                                        print(e)


