#!/usr/bin/env python3
"""
Lab 4:Q2B: reterieve a bucket pplicy
"""
import boto3
import json
s3= boto3.client('s3')  
bucket_name = 'cyu004lab4'  
bucket_policy = {
    'Version' : '2012-10-17',
    'Statement':[{
        'Sid':'AddPerm',
        'Effect':'Allow',
        'Principal':'*',
        'Action':['s3:getObject'],
        'Resource':"arn:aws:s3:::%s/*"%bucket_name
    }]
}

bucket_policy = json.dumps(bucket_policy)
s3.put_bucket_policy(Bucket=bucket_name,Policy=bucket_policy)
response = s3.get_bucket_policy(Bucket=bucket_name)
print(response['Policy'])
