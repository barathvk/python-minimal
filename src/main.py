import requests

r = requests.get('https://httpbin.org/ip')
print(r.json()['origin'])