import json
import jsonpath
import openpyxl
import requests
import py


def test_add_new_student():
    url = 'http://www.thetestingworldapi.com/api/studentsDetails'
    file = open("C:\\dev\\RecapAPIAutomation\\https://d.docs.live.net/e18a130ee1811b1c/Desktop/Test-data.xlsx", "r")
    json_request = json.loads(file.read())
    response = requests.post(url, json_request)
    print(response.status_code)
    assert response.status_code == 201
    wk = openpyxl.load_workbook(
        "C:\\dev\\RecapAPIAutomation\\https://d.docs.live.net/e18a130ee1811b1c/Desktop/Test-data.xlsx")
    sh = wk['Sheet1']
    rows = sh.max_row
    print(rows)
