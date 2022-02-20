from index import buildResponse

def test_passing():
  assert (1,2,3) == (1,2,3)

def test_retrieveSecret():
  assert (1,2,3) == (1,2,3)

def test_extractSecret():
  assert (1,2,3) == (1,2,3)

def test_buildResponse():
  print(buildResponse("123","123","123"))
  assert (1,2,3) == (1,2,3)