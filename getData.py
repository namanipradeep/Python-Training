import requests

response=requests.get('https://www.google.com')

print(response)

print(response.text)

print(response.status_code)

print(response.history)