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
import openpyxl
import pytest
import requests
import json
from Utilities import CommonUtilities

# URL
base_url = "https://thetestingworldapi.com/"


# Use this command in Terminal -> To generate JSON files for ALlure reports
#  python3 -m pytest -m Allure --html=Reports/PyTest/TestAutomation_API_PyTestHTML_Report.html --alluredir Reports/Allure

@pytest.mark.Allure
def test_01_Optimized_POST_DataDriven_MultipleDataSets_Using_XLSX_File():
    # Open the JSON file in READ mode
    file = open('files/03_DataDriven_Excel/01_AddStudent.json', 'r')

    # Read the content from the file
    input_JSON = file.read()

    # Convert txt format to JSON format
    requestBody_JSON = json.loads(input_JSON)

    obj = CommonUtilities('files/03_DataDriven_Excel/TestData.xlsx', 'AddStudent')
    rows = obj.fetch_row_count()
    print(obj.fetch_column_count())
    keyList = obj.fetch_key_names()

    # Not starting from Row 1 (because 1st row is Header)
    for index in range(2, rows + 1):
        updated_json_request = obj.update_request_with_data(index, requestBody_JSON, keyList)

        response = requests.post(base_url + "api/studentsDetails", updated_json_request)

        print(
            "===========>>>>>>>>>>>>> response.text ==>> " + response.text)

        # Assertion for Response Status Code
        assert response.status_code == 201
