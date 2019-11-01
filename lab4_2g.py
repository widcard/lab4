#!/usr/bin/env python3
"""
Lab 4:Q2B: list all Amazon S3 Buckets
"""
import boto3
bucket_name= 'cyu004lab4'
s3= boto3.client('s3')  
response = s3.get_bucket_acl(Bucket=bucket_name)
print(response)