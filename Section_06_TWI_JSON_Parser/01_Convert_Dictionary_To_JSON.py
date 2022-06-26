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

# Convert Dictionary to JSON

# json -> Package coming with Python
import json

# Data to be written
dictionary = {
    "id": "04",
    "name": "sunil",
    "department": "HR"
}

# Serializing json
json_object = json.dumps(dictionary, indent=4)
# json_object = json.dumps(dictionary)
print(json_object)

