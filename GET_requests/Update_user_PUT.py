import json

import jsonpath
import requests

# API url

url = "https://reqres.in/api/users/2"

# read input json file and turn it into json format
file = open("C:\\dev\\RecapAPIAutomation\\create_user.json", 'r')
json_input = file.read()
turnIntoJson = json.loads(json_input)
# print(turnIntoJson)

# Make PUT request with json_input

response_from_put_request = requests.put(url, turnIntoJson)
assert response_from_put_request.status_code == 200

# # Parse response to Json Format
response_json = json.loads(response_from_put_request.text)
print(response_json)
