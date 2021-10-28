import requests

# we first create a dictionary to include our new headers

headerdata = {"T1": "First_Header", "T2": "Second_Header"}

response_from_get = requests.get("http://httpbin.org/get", headers=headerdata)
print(response_from_get.text)
