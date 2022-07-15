# /**
# * @author Rajat Verma
# * https://www.linkedin.com/in/rajat-v-3b0685128/
# * https://github.com/rajatt95
# * https://rajatt95.github.io/
# * https://github.com/stars/rajatt95/lists/udemy-testing-world-infotech
# * https://github.com/rajatt95/Python_Requests_TWI
# *
# * Course: Step by Step Rest API Testing using Python + Pytest +Allure (https://www.udemy.com/course/api-testing-python/)
# * Tutor: Testing World Infotech (https://www.udemy.com/user/technology-world/)
# */
#
# /***************************************************/

# HTTP method GET call (with Customized Headers) using requests package

import requests
import json
import jsonpath

# URL
base_url = "https://thetestingworldapi.com/"

student_ID = str(2678624)


def test_01_POST_add_student_assert_response_status():
    # URL
    url = base_url + "api/studentsDetails"

    # Open the JSON file in READ mode
    file = open('../files/01_StudentManagementSystem/01_AddStudent.json', 'r')

    # Read the content from the file
    input_JSON = file.read()

    # Convert txt format to JSON format
    requestBody_JSON = json.loads(input_JSON)

    print(requestBody_JSON)  # {'first_name': 'Rajat', 'middle_name': '-', 'last_name': 'Verma', 'date_of_birth':
    # '05/02/1995'}

    # Send POST Request with Request body
    response = requests.post(url, requestBody_JSON)

    # Print the Response Text
    print(
        "===========>>>>>>>>>>>>> response.text ==>> " + response.text)  # {"id":2678616,"first_name":"Rajat","middle_name":"-",
    # "last_name":"Verma", "date_of_birth":"05/02/1995"}

    # Print the Response Status Code
    print(response.status_code)  # 201

    # Assertion for Response Status Code
    assert response.status_code == 201

    # print('##################################################')


def test_02_GET_student_details_assert_response_status_AND_response_body():
    # URL
    url = base_url + "api/studentsDetails/" + student_ID
    # url = base_url + "api/studentsDetails/2678620"

    # Send GET Request
    response = requests.get(url)

    # Print the Response Text
    print("===========>>>>>>>>>>>>> response.text ==>> " + response.text)  # response.text ==>> {"status":"true",
    # "data":{"id":2678620,"first_name":"Rajat","middle_name":"-","last_name":"Verma","date_of_birth":"05/02/1995"}}

    # Print the Response Status Code
    print(response.status_code)  # 200

    # Assertion for Response Status Code
    assert response.status_code == 200

    print("================================")

    # Parse Response into JSON format
    # response_json = json.loads(response.text)
    response_json = response.json()
    print(response_json)  # {'status': 'true', 'data': {'id': 2678620, 'first_name': 'Rajat', 'middle_name': '-',
    # 'last_name': 'Verma', 'date_of_birth': '05/02/1995'}}

    print("================================")

    # Using JSONPath to reach specific point
    actual_ID = jsonpath.jsonpath(response_json, 'data.id')
    print(actual_ID[0])
    assert str(actual_ID[0]) == student_ID


def test_03_PUT_update_student_assert_response_status_AND_response_body():
    # URL
    url = base_url + "api/studentsDetails/" + student_ID

    # Open the JSON file in READ mode
    file = open('../files/01_StudentManagementSystem/02_UpdateStudent.json', 'r')

    # Read the content from the file
    input_JSON = file.read()

    # Convert txt format to JSON format
    requestBody_JSON = json.loads(input_JSON)

    print(requestBody_JSON)  # {'id': 2678620, 'first_name': 'Updated Rajat', 'middle_name': '-', 'last_name':
    # 'Updated Verma', 'date_of_birth': '05/02/1995'}

    # Send PUT Request with Request body
    response = requests.put(url, requestBody_JSON)

    # Print the Response Text
    print(
        "===========>>>>>>>>>>>>> response.text ==>> " + response.text)  # ===========>>>>>>>>>>>>> response.text
    # ==>> {"status":"true","msg":"update  data success"}

    # Print the Response Status Code
    print(response.status_code)  # 200

    # Assertion for Response Status Code
    assert response.status_code == 200

    print("================================")

    # Using JSONPath to reach specific point
    actual_Msg = jsonpath.jsonpath(response.json(), 'msg')
    print(actual_Msg[0])
    assert str(actual_Msg[0]) == "update  data success"


def test_04_DELETE_delete_student_assert_response_status_AND_response_body():
    # URL
    url = base_url + "api/studentsDetails/" + student_ID

    # Send DELETE Request with Request body
    response = requests.delete(url)

    # Print the Response Text
    print(
        "===========>>>>>>>>>>>>> response.text ==>> " + response.text)  # ===========>>>>>>>>>>>>> response.text
    # ==>> {"status":"true","msg":"Delete  data success"}

    # Print the Response Status Code
    print(response.status_code)  # 200

    # Assertion for Response Status Code
    assert response.status_code == 200

    print("================================")

    # Using JSONPath to reach specific point
    actual_Msg = jsonpath.jsonpath(response.json(), 'msg')
    print(actual_Msg[0])
    assert str(actual_Msg[0]) == "Delete  data success"
