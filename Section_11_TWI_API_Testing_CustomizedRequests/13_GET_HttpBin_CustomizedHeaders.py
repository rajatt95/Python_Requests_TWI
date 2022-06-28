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

# HTTP method GET call (with Customized Headers) using requests package

import requests
import json
import jsonpath

# URL
url = "https://httpbin.org/get"

# Custom Headers
data_headers = {'custom_header_key_1': 'custom_header_value_1', 'custom_header_key_2': 'custom_header_value_2'}

# Send GET Request with Customized Headers
response = requests.get(url, headers=data_headers)
# response = requests.get(url, headers={"Custom-Content-Type": "text"})

# Print the Response Status Code
print(response.status_code)  # 200

# Assertion for Response Status Code
assert response.status_code == 200

print('##################################################')
# Get the Response Headers
print(response.headers)

# Get the specific Response Header
print(response.headers.get("Content-Type"))  # application/json; charset=utf-8
print(response.headers.get("Connection"))  # keep-alive

# ISSUE
# print(response.headers.get("Custom-Content-Type"))  # None
print(response.headers.get("custom_header_key_1"))  # None

print('##################################################')
# Print the Response Text
print(response.text)
