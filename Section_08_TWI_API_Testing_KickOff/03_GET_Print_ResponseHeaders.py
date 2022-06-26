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

# URL
import requests

url = "https://reqres.in/api/users?page=2"

# Send GET Request
response = requests.get(url)

# Get the Response Headers
print(response.headers)

# Get the specific Response Header
print(response.headers.get("Content-Type"))  # application/json; charset=utf-8
print(response.headers.get("Connection"))  # keep-alive
