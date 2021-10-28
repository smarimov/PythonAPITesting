import requests
import json
import jsonpath


def test_Add_new_student():
    url = 'http://www.thetestingworldapi.com/api/studentsDetails'
    file = open("C:\\dev\\RecapAPIAutomation\\input_data_for_put_api.json", "r")
    request_json = json.loads(file.read())
    response_from_post = requests.post(url, request_json)
    id = jsonpath.jsonpath(response_from_post.json(), 'id')
    print(id[0])

    # This adds technical details:
    tech_api_url = 'http://www.thetestingworldapi.com/api/technicalskills'
    file = open("C:\\dev\\RecapAPIAutomation\\tech_details_input.json", "r")
    # we turn this into json file as a request for PUT calls to add technical details:
    request_json = json.loads(file.read())
    request_json['id'] = int(id[0])  # instead of changing id in the notepad++, this adds dynamically changing ids
    request_json['st_id'] = id[0]  # here we didn't turn it into integer, as format shows it should be string

    response_from_post = requests.post(tech_api_url, request_json)
    print(response_from_post.text)

    # this adds student's address:
    address_api_url = 'http://www.thetestingworldapi.com/api/addresses'
    file = open("C:\\dev\\RecapAPIAutomation\\address_input.json", "r")
    # we turn this into json file as a request for PUT calls to add technical details:
    request_json = json.loads(file.read())
    request_json['stId'] = id[0]  # same here for dynamic id changing
    response_from_post = requests.post(address_api_url, request_json)
    print(response_from_post.text)

    # this gets final info about the student
    final_details_url = 'http://www.thetestingworldapi.com/api/FinalStudentDetails/' + str(id[0])
    response_from_get = requests.get(final_details_url)
    print(response_from_get.text)
