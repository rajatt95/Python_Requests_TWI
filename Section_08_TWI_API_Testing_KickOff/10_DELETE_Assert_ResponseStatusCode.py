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

# HTTP method DELETE call using requests package

import requests

# URL
url = "https://reqres.in/api/users/2"

# Send DELETE Request
response = requests.delete(url)

# Print the Response Status Code
print(response.status_code) # 204

# Assertion for Response Status Code
assert response.status_code == 204

