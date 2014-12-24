curl -X POST -d "name=yhf&password=1234" -i http://localhost:5000/api/account/login  # username empty
curl -X POST -d "username=yhf&pass=1234" -i http://localhost:5000/api/account/login  # password empty
curl -X POST -d "username=abcd&password=1" -i http://localhost:5000/api/account/login  # use not exist
curl -X POST -d "username=yhf&password=1234" -i http://localhost:5000/api/account/login  # wrong password
curl -X POST -d "username=yhf&password=123" -i http://localhost:5000/api/account/login   # login OK

curl -X POST -d "username=aaaaabbbbbaaaaabbbbba&password=123" -i http://localhost:5000/api/account/register  # username too long
curl -X POST -d "username=aaaaa&password=aaaaabbbbbaaaaabbbbba" -i http://localhost:5000/api/account/register  # password too long
curl -X POST -d "username=yhf&password=123" -i http://localhost:5000/api/account/register   # username exists
curl -X POST -d "username=yhf09&password=123" -i http://localhost:5000/api/account/register  # register OK
