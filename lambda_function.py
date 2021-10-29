import json
import boto3
import urllib.parse
from urllib.parse import urlparse
from urllib.parse import unquote_plus

s3 = boto3.client('s3')
s3.upload_file('out.zip','deployment-of-aws-code','lambda_function.py')
def handler(event, context):
    # TODO implement
key_name = unquote_plus(event['Records'][0]['s3']['object']['key'])
S3: {
 "bucket": {
   "name": "deployment-of-aws-code"
  },
  "object": {
    "key": "out.zip"
  }     
 #my-first-test
 #this is for test purpose
}
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
