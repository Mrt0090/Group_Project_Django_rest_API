Modifications from Julie:

mobiles/models.py

added:

```
def __str__(self):

        return f"{self.brand} {self.model}"
```

reviews.py/models.py


```def __str__(self):
        return f"Review by {self.author} on {self.phone}"
```

## Test Authentication Endpoints
Now you can test the following API endpoints:

User Login: POST /api/accounts/users/login/
```json

{
  "username": "testuser",
  "password": "password123"
}
```
+ User Logout: POST /api/accounts/users/logout/
+ User Registration: POST /api/accounts/users/registration/
```json

{
  "username": "testuser",
  "password1": "password123",
  "password2": "password123"
}
```
+ Password Reset: POST /api/accounts/users/password/reset/
+ Token Authentication (if needed):
```sh

curl -X POST -H "Content-Type: application/json" -d '{"username":"testuser", "password":"password123"}' http://127.0.0.1:8000/api/accounts/users/login/
```


### Run this code according to the assigned Database (as of now)

At settings.py, if database is set to sqlite3, run this way: goto Terminal, make sure you are at the manage.py folder level, source .venv/bin/activate, then --->
```
python manage.py runserver 8080
```
if not, run this way:
```
docker-compose up --build
```
