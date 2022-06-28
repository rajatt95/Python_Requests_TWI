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

# HTTP method GET call (with Query Parameters) using requests package

import requests

# URL
url = "https://httpbin.org/get"

# Custom Parameters
queryParams = {'name': 'Rajat Verma', 'profile-github': 'https://github.com/rajatt95'}

# Send GET Request with Query parameters
response = requests.get(url, params=queryParams)

print('##################################################')
# Print the Response Text
print(response.text)

