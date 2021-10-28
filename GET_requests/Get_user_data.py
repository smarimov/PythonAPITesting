import requests
import json
import jsonpath

# API URL
url = "https://reqres.in/api/users?page=2"

# Send Get request

get_response = requests.get(url)

# Display response content
# print(get_response.content)

# Display Header

# print(get_response.headers)

# Validate status code
assert get_response.status_code == 200

# # Get response header
# # print(get_response.headers)
#
# # Get specific response header
#
# print(get_response.headers.get('Date'))
# print(get_response.headers.get('Server'))
#
#
# #Get elapsed time
# print(get_response.elapsed)

# Parse response to json format

json_response = json.loads(get_response.text)
# print(json_response)

# Fetch value using Json Path

pages = jsonpath.jsonpath(json_response, "total_pages")
#assert pages[0] == 2

# advanved fetching using json path

for i in range(0,3):
    first_name = jsonpath.jsonpath(json_response, "data[i].first_name")
    print(first_name)



