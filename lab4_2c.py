"""
Lab4 Q2c : upload files to an amazon s3 bucket
"""

import boto3
s3 = boto3.client('s3')

filename = 'README.md'

bucket_name = 'cyu004lab4'
s3.upload_file(filename, bucket_name, filename)