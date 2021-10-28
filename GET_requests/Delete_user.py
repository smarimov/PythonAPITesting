import requests

# API url
url = "https://reqres.in/api/users/2"

response_after_delete = requests.delete(url)

print(response_after_delete)

assert  response_after_delete.status_code == 204