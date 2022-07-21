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

import requests
import json
import jsonpath

# URL
base_url = "https://thetestingworldapi.com/"


def test_01_POST_add_student():
    global student_ID_String_ToBeUsed_In_OtherRequests

    # Send POST Request with Request body
    response = requests.post(base_url + "api/studentsDetails",
                             json.loads(open('../files/02_E2E/01_AddStudent.json', 'r').read()))

    # Print the Response Text
    print("===========>>>>>>>>>>>>> response.text ==>> " + response.text)

    # Assertion for Response Status Code
    assert response.status_code == 201, "Assertion for Response Status Code"

    student_ID = jsonpath.jsonpath(response.json(), 'id')
    print("str(student_ID[0]) in String")
    print(str(student_ID[0]))  # This is returning the value in String
    print("int(student_ID[0]) in Integer")
    print(int(student_ID[0]))  # This is returning the value in integer

    student_ID_String_ToBeUsed_In_OtherRequests = str(student_ID[0])


# Student ID - Fetched from previous API call ->
# Will be used here in GET request (As Path Parameter)
def test_02_GET_student_FinalDetails():
    response = requests.get(base_url + "api/studentsDetails/" + student_ID_String_ToBeUsed_In_OtherRequests)

    print(
        "===========>>>>>>>>>>>>> response.text ==>> " + response.text)

    # Assertion for Response Status Code
    assert response.status_code == 200, "Assertion for Response Status Code"
    # Assertion for Student ID
    assert response.json()['data']['id'] == int(student_ID_String_ToBeUsed_In_OtherRequests)
