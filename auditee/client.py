import requests

# test upload
with open('testproof') as fp:
    content = fp.read()

response = requests.post(
    'http://127.0.0.1:5000/upload/testproof', data=content
)

print("upload response:",response.status_code)

# test download
response = requests.get(
    'http://127.0.0.1:5000/download/testproof'
)
print("download response:", response);
