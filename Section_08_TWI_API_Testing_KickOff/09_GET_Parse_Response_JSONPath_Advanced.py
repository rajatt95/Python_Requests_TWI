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

# HTTP method GET call using requests package

import requests
import json
import jsonpath

# URL
url = "https://reqres.in/api/users?page=2"

# Send GET Request
response = requests.get(url)

# Parse Response into JSON format
response_json = json.loads(response.text)
print(response_json)

print("================================")

# Using JSONPath to reach specific point
print(jsonpath.jsonpath(response_json, 'per_page'))  # [6]
print(jsonpath.jsonpath(response_json, 'total_pages'))  # [2]

print(jsonpath.jsonpath(response_json, 'data[0].first_name'))  # ['Michael']
print(jsonpath.jsonpath(response_json, 'data[1].first_name'))  # ['Lindsay']
print(jsonpath.jsonpath(response_json, 'data[2].first_name'))  # ['Tobias']

print("================================ LOOP - FOR ")
for index in range(0, 3):
    first_name = jsonpath.jsonpath(response_json, 'data[' + str(index) + '].first_name')
    print(first_name[0])
