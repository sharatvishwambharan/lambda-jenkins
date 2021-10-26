import json
import boto3
import urllib.parse
from urllib.parse import urlparse
from urllib.parse import unquote_plus

def handler(event, context):
    # TODO implement
key_name = unquote_plus(event['Records'][0]['s3']['object']['key'])
S3: {
 "bucket": {
   "name": "deployment-of-aws-code"
  },
  "object": {
    "key": "out.zip/lambda_function.py"
  }
 #my-first-test
}
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
