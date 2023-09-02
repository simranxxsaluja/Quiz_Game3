# 4. in line 3 of this code file, in the quotation marks, paste the link for path of the extension
import sys
sys.path.append(r"c:\users\simsa\appdata\local\packages\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\localcache\local-packages\python311\site-packages")
import requests

usingopendtb = False
question_data = []
if usingopendtb:
    parameters = {
        "amount": 10,
        "type": "multiple"
    }

    response = requests.get(url="https://opentdb.com/api.php?amount=10", params=parameters)
    question_data = response.json()["results"]
else:
    response = requests.get(url="https://sheet2api.com/v1/RbUpSfgxS9mT/data")
    temp = response.json()
    for item in temp:
        incorrect_answers = []
        if item["incorrect_answers.0"] != None and item["incorrect_answers.0"] != "":
            incorrect_answers.append(str(item["incorrect_answers.0"]).capitalize())
        if item["incorrect_answers.1"] != None and item["incorrect_answers.1"] != "":
            incorrect_answers.append(str(item["incorrect_answers.1"]).capitalize())
        if item["incorrect_answers.2"] != None and item["incorrect_answers.2"] != "":
            incorrect_answers.append(str(item["incorrect_answers.2"]).capitalize())
        item["incorrect_answers"]=incorrect_answers
    question_data = temp
#may have to go back and manually code if want to randomly put in the questions for else clause section
