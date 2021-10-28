import pytest
import requests
import json
import jsonpath


def test_add_student_data():
    # API url
    url = "http://www.thetestingworldapi.com/api/studentsDetails"
    file = open("C:\\dev\\RecapAPIAutomation\\input_data_for_put_api.json", "r")
    # this turns the file into json file:
    json_file = json.loads(file.read())
    response_from_POST = requests.post(url, json_file)
    print(response_from_POST.text)


def test_update_student_details():
    # API url
    url = "http://www.thetestingworldapi.com/api/studentsDetails/524944"
    file = open("C:\\dev\\RecapAPIAutomation\\input_data_for_put_api.json", "r")
    # this turns the file into json file:
    json_file = json.loads(file.read())
    response_from_PUT = requests.put(url, json_file)
    print(response_from_PUT.text)


def test_delete_student_details():
    # API URL
    url = 'http://www.thetestingworldapi.com/api/studentsDetails/524944'
    response_from_delete = requests.delete(url)
    print(response_from_delete.text)


def test_get_student_data():
    # API URL
    url = 'http://www.thetestingworldapi.com/api/studentsDetails/524944'
    response_from_get = requests.get(url)
    turn_into_json = json.loads(response_from_get.text)
    print(response_from_get.text)
    id = jsonpath.jsonpath(turn_into_json, 'data.id')
    assert id[0] == 524944
