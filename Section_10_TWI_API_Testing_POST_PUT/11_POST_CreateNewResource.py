# /**
# * @author Rajat Verma
# * https://www.linkedin.com/in/rajat-v-3b0685128/
# * https://github.com/rajatt95
# * https://rajatt95.github.io/
# * https://github.com/stars/rajatt95/lists/udemy-testing-world-infotech
# *
# * Course: Step by Step Rest API Testing using Python + Pytest +Allure (https://www.udemy.com/course/api-testing-python/)
# * Tutor: Testing World Infotech (https://www.udemy.com/user/technology-world/)
# */
#
# /***************************************************/

# HTTP method POST call using requests package

import requests
import json
import jsonpath

# URL
url = "https://reqres.in/api/users"

# Open the JSON file in READ mode
file = open('../files/01_ReqRes_POST.json', 'r')

# Read the content from the file
input_JSON = file.read()

# Convert txt format to JSON format
requestBody_JSON = json.loads(input_JSON)

print(requestBody_JSON)  # {'name': 'morpheus', 'job': 'leader'}

# Send POST Request with Request body
response = requests.post(url, requestBody_JSON)

# Print the Response Status Code
print(response.status_code)  # 201

# Assertion for Response Status Code
assert response.status_code == 201

print('##################################################')
# Get the Response Headers
print(response.headers)

# Get the specific Response Header
print(response.headers.get("Content-Type"))  # application/json; charset=utf-8
print(response.headers.get("Connection"))  # keep-alive
print('##################################################')

# Print the Response Content
print(response.content)  # b'{"name":"morpheus","job":"leader","id":"754","createdAt":"2022-06-28T12:32:15.697Z"}'
print('##################################################')

# Parse Response into JSON format
response_json = json.loads(response.text)
print(response_json)

print("================================")

# Using JSONPath to reach specific point
print(jsonpath.jsonpath(response_json, 'name'))  # ['morpheus']
print(jsonpath.jsonpath(response_json, 'job'))  # ['leader']