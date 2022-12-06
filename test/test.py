import requests

# Welcome Test
x = requests.get('http://localhost:5000/')
print(x.status_code)
print(x.headers)
print(x.text)
