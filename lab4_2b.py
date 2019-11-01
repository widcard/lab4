#!/usr/bin/env python3
"""
Lab 4:Q2B: list all Amazon S3 Buckets
"""
import boto3
s3_client = boto3.client('s3')
response= s3_client.list_buckets()

print('Existing buckets')
for bucket in response['Buckets']:
    print(f'{bucket["Name"]}')
