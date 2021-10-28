import json
import requests
import jsonpath


def test_outh_api():
    # this url provides token:
    token_url = 'http://www.thetestingworldapi.com/Token'
    data = {'grant_type': 'password', 'username': 'admin', 'password': 'level123#'}
    response = requests.post(token_url, data)
    print(response.text)

    url = 'http://www.thetestingworldapi.com/api/StDetails/1104'
    response = requests.get(url)
    print(response.text)
