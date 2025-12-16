from jose import jwt

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

payload = {"sub": 1}  # Replace 1 with your user's ID
token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
print(token)
