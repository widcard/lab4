"""
lab4: Q1B: start amd stop detailed monitoring of an ec2 instance~
QA
"""
import sys
import boto3
ec2 = boto3.client('ec2')
if sys.argv[1] =='ON':
    response = ec2.monitor_instances(InstanceIds=['i-0406ee5fad24569a9'])
else:
    response = ec2.unmonitor_instances(InstanceIds=['i-0406ee5fad24569a9'])
print(response)