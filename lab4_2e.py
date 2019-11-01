#!/usr/bin/env python3
"""
Lab 4:Q2e: reate presigned ULRs
"""
import boto3
import logging

bucket_name ='cyu004lab4'
key ='README.md'
s3 = boto3.client('s3')
responce = s3.generate_presigned_url(ClientMethod='get_object',Params={
    'Bucket':bucket_name,
    'Key':key})
print(responce)
