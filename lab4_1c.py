"""
lab4: Q1c: start amd stop detailed monitoring of an ec2 instance~
QA
"""
import sys
import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')
action = sys.argv[1].upper()
if action =='ON':
    # Do a dryrun first to verify permissions
    try:
        ec2.start_instances(InstanceIds=['i-0a8ca4b5868c96b5b'], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise
    #Dryr run succeeded, run start_instance again without dryrun
    try:
        response = ec2.start_instances(InstanceIds=['i-0a8ca4b5868c96b5b'], DryRun=False)
        print(response)
    except ClientError as e:
        print(e)
else:
    try:
        ec2.stop_instances(InstanceIds=['i-0a8ca4b5868c96b5b'], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise
    #Dryr run succeeded, run start_instance again without dryrun
    try:
        response = ec2.stop_instances(InstanceIds=['i-0a8ca4b5868c96b5b'], DryRun=False)
        print(response)
    except ClientError as e:
        print(e)
