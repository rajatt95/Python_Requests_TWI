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

# 3 APIs included

    # 1. POST - Add Student
        # Request body will be sent using JSON file - ../files/02_E2E/01_AddStudent.json

    # 2. POST - Add Technical Skills to the Student created
        # Request body will be sent using JSON file - ../files/02_E2E/02_AddTechnicalSkills.json
            # Also, id (int) and st_id (String) are two keys in JSON file
                # We will update them before making the API call,
                    # So that, for every new Student created by add_student API -> Technical Skills will be added

    # 3. GET - Get the final details of that Student
        # Student ID (String) will be passed in Path Parameter

def test_E2E_01_add_student_02_add_TechnicalSkills_03_Get_FinalDetails():
    # ===============>>>>>>>>>>>>>>>>> 1. ADD STUDENT DETAILS
    print("===============>>>>>>>>>>>>>>>>> 1. ADD STUDENT DETAILS")

    # Send POST Request with Request body
    response_POST_Add_Student = requests.post(base_url + "api/studentsDetails",
                                              json.loads(open('../files/02_E2E/01_AddStudent.json', 'r').read()))

    # Print the Response Text
    print(
        "===========>>>>>>>>>>>>> response.text ==>> " + response_POST_Add_Student.text)  # {"id":2678616,"first_name":"Rajat","middle_name":"-",
    # "last_name":"Verma", "date_of_birth":"05/02/1995"}

    # Assertion for Response Status Code
    assert response_POST_Add_Student.status_code == 201, "Assertion for Response Status Code"

    student_ID = jsonpath.jsonpath(response_POST_Add_Student.json(), 'id')
    print("student_ID[0] in String")
    print(student_ID[0])  # This is returning the value in String
    print("student_ID[0] in Integer")
    print(int(student_ID[0]))  # This is returning the value in integer

    # ===============>>>>>>>>>>>>>>>>> 2. ADD TECHNICAL SKILLS
    print("===============>>>>>>>>>>>>>>>>> 2. ADD TECHNICAL SKILLS")

    # In 02_AddTechnicalSkills.json file, there are 2 keys
    #     1. id
    #     2. st_id
    #           We have to make values for these keys DYNAMIC
    #           These values should be set from the 1st test (test_01_POST_add_student)

    # Convert txt format to JSON format
    requestBody_JSON = json.loads(open('../files/02_E2E/02_AddTechnicalSkills.json', 'r').read())

    # Updating id and st_id DYNAMICALLY
    # This will be set from the previous API call
    requestBody_JSON['id'] = int(student_ID[0])  # This is returning the value in Integer
    requestBody_JSON['st_id'] = student_ID[0]  # This is returning the value in String

    print(requestBody_JSON)

    # Send POST Request with Request body
    response_POST_Add_TechnicalSkills = requests.post(base_url + "api/technicalskills", requestBody_JSON)

    # Print the Response Text
    print(
        "===========>>>>>>>>>>>>> response_POST_Add_TechnicalSkills.text ==>> " + response_POST_Add_TechnicalSkills.text)  # {"id":2678616,"first_name":"Rajat","middle_name":"-",
    # "last_name":"Verma", "date_of_birth":"05/02/1995"}

    # Assertion for Response Status Code
    assert response_POST_Add_TechnicalSkills.status_code == 200, "Assertion for Response Status Code"

    print(response_POST_Add_TechnicalSkills.text)
    # Using JSONPath to reach specific point
    assert jsonpath.jsonpath(response_POST_Add_TechnicalSkills.json(), 'status')[0] == "true"
    assert jsonpath.jsonpath(response_POST_Add_TechnicalSkills.json(), 'msg')[0] == "Add  data success"

    # ===============>>>>>>>>>>>>>>>>> 3. GET FINAL DETAILS OF STUDENT
    print("===============>>>>>>>>>>>>>>>>> 3. GET FINAL DETAILS OF STUDENT")

    # Send GET Request with Student ID ( In Path Parameter)
    response_GET_FinalDetails_Student = requests.get(base_url + "api/FinalStudentDetails/"+str(student_ID[0]))

    # Print the Response Text
    print(
        "===========>>>>>>>>>>>>> response_GET_FinalDetails_Student.text ==>> " + response_GET_FinalDetails_Student.text)  # {"id":2678616,"first_name":"Rajat","middle_name":"-",
    # "last_name":"Verma", "date_of_birth":"05/02/1995"}

    # Assertion for Response Status Code
    assert response_GET_FinalDetails_Student.status_code == 200, "Assertion for Response Status Code"

    # Using JSONPath to reach specific point
    assert jsonpath.jsonpath(response_GET_FinalDetails_Student.json(), 'status')[0] == "true"
