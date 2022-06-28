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

# HTTP method PUT call using requests package

import requests
import json
import jsonpath

# URL
url = "https://reqres.in/api/users/2"

# Open the JSON file in READ mode
file = open('../files/02_ReqRes_PUT.json', 'r')

# Read the content from the file
input_JSON = file.read()

# Convert txt format to JSON format
requestBody_JSON = json.loads(input_JSON)

print(requestBody_JSON)  # {'name': 'Updated - morpheus', 'job': 'Updated - leader'}

# Send PUT Request with Request body
response = requests.put(url, requestBody_JSON)

# Print the Response Status Code
print(response.status_code)  # 200

# Assertion for Response Status Code
assert response.status_code == 200

print('##################################################')

# Parse Response into JSON format
response_json = json.loads(response.text)
print(response_json)

print("================================")

# Using JSONPath to reach specific point
print(jsonpath.jsonpath(response_json, 'name'))  # ['Updated - morpheus']
print(jsonpath.jsonpath(response_json, 'job'))  # ['Updated - leader']