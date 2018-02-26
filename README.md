# API Auth Test

This is a simple test for API authentication using Basic HTTP to carry the API token and MongoDB as database.

To run this example, make sure you have MongoDB 3.4+ running on port 27017

* Note: No auth is used for MongoDB in this example. 
To configure MongoDB settings please refer to 
[Djongo Documentation](https://nesdis.github.io/djongo/database-configuration/)



## Set up Database

```
python manage.py makemigrations
python manage.py migrate
```

Create "test" user

```
python manage.py createsuperuser
user: test
pwd: testonly
```

## Create API key

```
python manage.py runserver
```

Access with "test" user in your browser

```
http://127.0.0.1:8000/admin
```

Select user "test" and add api client

```
API key: abcdefgh123456789
```

Edit user "test" and add first and last name: "Peter Pan"


## Test API


#### Simple end point

```
curl -X GET http://127.0.0.1:8000/api/ -w "\n"
```

output:

```
{"api": "Test V1", "timestamp": 1519673841}
```

#### Auth endpoint with invalid API key

```
curl -u test:not_valid -X GET http://127.0.0.1:8000/api/hello -w "\n"
```

output:

```
{"error": "Invalid authorization token provided"}
```

#### Auth endpoint with correct API key

```
curl -u test:abcdefgh123456789 -X GET http://127.0.0.1:8000/api/hello -w "\n"
```

output:

```
{"msg": "Hello Peter Pan"}
```
