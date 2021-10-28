import json

import jsonpath
import requests

# API url

url = "https://reqres.in/api/users"

# read input json file and turn it into json format
file = open("C:\\dev\\RecapAPIAutomation\\create_user.json", 'r')
json_input = file.read()
turnIntoJson = json.loads(json_input)
# print(turnIntoJson)

# Make Post request with json_input

response_from_post_request = requests.post(url, turnIntoJson)
assert response_from_post_request.status_code == 201

# Parse response to Json Format
response_json = json.loads(response_from_post_request.text)
id = jsonpath.jsonpath(response_json, 'id')
print(id[0])
