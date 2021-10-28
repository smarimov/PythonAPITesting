import json
import jsonpath
import requests


def test_add_student_data():
    global id  # this makes the id usable in any methods
    # API url
    url = "http://www.thetestingworldapi.com/api/studentsDetails"
    file = open("C:\\dev\\RecapAPIAutomation\\add_student.json", "r")
    # this turns the file into json file:
    json_file = json.loads(file.read())
    response_from_POST = requests.post(url, json_file)
    id = jsonpath.jsonpath(response_from_POST.json(), 'id')
    print(id[0])


def test_get_student_details():
    url = 'http://www.thetestingworldapi.com/api/studentsDetails/' + str(id[0])
    response_from_get = requests.get(url)
    print(response_from_get.text)
