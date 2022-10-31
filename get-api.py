import requests

headers = {
  'Content-Type': 'application/json',
  'x-auth-token': '\'token\''
}

response = requests.get('https://staging.smartkungahara.rw/core/api/v1.1/gaps', headers=headers)

print(response.status_code)
print(response.headers)
print(response.json())