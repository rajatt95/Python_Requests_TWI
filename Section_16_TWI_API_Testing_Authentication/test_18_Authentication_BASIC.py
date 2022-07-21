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
from requests.auth import HTTPBasicAuth

def test_Validate_ResponseMessage_Without_Authentication():
    response = requests.get("https://api.github.com/user")
    print(response.text)
    print(response.status_code)
    # Assertions
    assert response.status_code == 401
    assert response.json()['message'] == 'Requires authentication'


def test_Validate_ResponseMessage_With_Authentication():
    response = requests.get("https://api.github.com/user",
                            auth=HTTPBasicAuth('your-username', 'your-password'))

    print(response.text)
    print(response.status_code)
    # Assertions
    # assert response.status_code == 401
    # assert response.json()['message'] == 'Requires authentication'
