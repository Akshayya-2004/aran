from app.auth import create_access_token, decode_access_token

token = create_access_token(
    {
        "sub": "akshayya@gmail.com"
    }
)

print("Token:")
print(token)

print()

payload = decode_access_token(token)

print("Payload:")
print(payload)