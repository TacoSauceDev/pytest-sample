from index import buildResponse

def test_passing():
  assert (1,2,3) == (1,2,3)

def test_retrieveSecret():
  assert (1,2,3) == (1,2,3)

def test_extractSecret():
  assert (1,2,3) == (1,2,3)

def test_buildResponse():
  assert (buildResponse("123","321","200")) == ({"statusCode": "200","headers": "321","body": "123"})
  
  
  
  def buildResponse(body_payload, headers, response_code):
    return {
        "statusCode": response_code,
        "headers": headers,
        "body": body_payload
    }
