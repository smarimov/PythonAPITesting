import requests

parameters = {'name': 'shokir', 'number': '78977-22-22'}

response_from_getrequest = requests.get("http://httpbin.org/get", params=parameters)
print(response_from_getrequest.text) 