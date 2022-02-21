from index import buildResponse
from index import retrieveSecret
from index import extractSecret
from moto import mock_secretsmanager
import json
import boto3

def test_passing():
  assert (1,2,3) == (1,2,3)

@mock_secretsmanager
def test_retrieveSecret():
  session = boto3.session.Session()
  client = session.client(service_name='secretsmanager',region_name='us-west-2')
  client.create_secret(
    Name = 'TestSecret',
    SecretString = '{"CostCenter":"12345"}',
  )
  secret = json.loads(retrieveSecret('TestSecret', client)['SecretString'])
  assert (secret['CostCenter'] == "12345")

@mock_secretsmanager
def test_extractSecret():
  secret = {"SecretString" : {"CostCenter":"12345"}}
  secretExtracted = extractSecret(secret, "CostCenter")
  assert (secretExtracted == "12345")

def test_buildResponse():
  assert (buildResponse("123","321","200")) == ({"statusCode": "200","headers": "321","body": "123"})

test_extractSecret()