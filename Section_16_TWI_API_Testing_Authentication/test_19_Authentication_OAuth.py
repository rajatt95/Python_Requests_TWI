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

# URL
base_url = "https://thetestingworldapi.com/"


def test_Validate_ResponseMessage_Without_Authentication():
    response = requests.get(base_url + "api/StDetails/1104")
    print(response.text)
    print(response.status_code)
    # Assertions
    assert response.status_code == 401
    assert response.json()['Message'] == 'Authorization has been denied for this request.'


# Send a Request and get Authorization Token
# Pick this token and store it in a variable
# Pass this token as Header in other requests

def get_Auth_Access_Token():
    # Username, Password and Grant type are required to get the access token
    data = {
        'grant_type': 'password',
        'username': 'admin',
        'password': 'admin'
    }

    # Tutor has not exposed the password -
    # Due to which, we are unable to get the access token

    url = base_url + "Token"
    response = requests.post(url, data)
    print(response.text)
    print(response.status_code)

    # assert response.status_code == 400
    # assert response.json()['error'] == 'invalid_grant'
    # assert response.json()['error_description'] == 'The user name or password is incorrect.'
    return 'Bearer ' + response.json()['access_token']


def test_Validate_ResponseMessage_With_Authentication():
    auth = {
        'Authorization': get_Auth_Access_Token()
    }
    response = requests.get(
        base_url + "api/StDetails/1104",
        headers=auth)
    print(response.text)
    print(response.status_code)
    # Assertions
    assert response.status_code == 401
    assert response.json()['Message'] == 'Authorization has been denied for this request.'
