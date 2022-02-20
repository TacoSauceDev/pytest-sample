# Purpose: To retrieve a secret from AWS Secrets Manager assuming you are running it from inside a lambda function
# This function is exceptionally verbose to give multiple points to unit test for the example.

import boto3 
import json 
import os

# Inputs -- you should have three variables come in from os.environ variables --
# os.environ('secretId')
# os.environ('secretValueName')
# os.environ('headerValues')
session = boto3.session.Session()
client = session.client(service_name='secretsmanager',region_name='us-west-2')

def handler(event, context):
    secret = retrieveSecret(os.environ['secretId'])
    secretExtracted = extractSecret(secret, os.environ['secretValueName'])
    return buildResponse(secretExtracted, os.environ['headerValues'], '200')

def retrieveSecret(secretId):
    return client.get_secret_value(SecretId=secretId)

def extractSecret(secret, secretValueName):
    secrets = json.loads(secret['SecretString'])
    return secrets[secretValueName]


def buildResponse(body_payload, headers, response_code):
    return {
        "statusCode": response_code,
        "headers": headers,
        "body": body_payload
    }
