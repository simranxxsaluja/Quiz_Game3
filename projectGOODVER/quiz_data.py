# 4. in line 3 of this code file, in the quotation marks, paste the link for path of the extension
import sys
sys.path.append(r"c:\users\simsa\appdata\local\packages\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\localcache\local-packages\python311\site-packages")
import requests

parameters = {
    "amount": 10,
    "type": "multiple"
}

response = requests.get(url="https://opentdb.com/api.php?amount=10", params=parameters)
question_data = response.json()["results"]
"""
Sample Response

[
    {
        'category': 'Sports', 
        'type': 'multiple', 
        'difficulty': 'medium', 
        'question': 'Which Formula One driver was nicknamed &#039;The Professor&#039;?',
        'correct_answer': 'Alain Prost', 
        'incorrect_answers': [
            'Ayrton Senna', 
            'Niki Lauda', 
            'Emerson Fittipaldi'
            ]
    }, 
    {
        'category': 'Entertainment: Music', 
        'type': 'multiple', 
        'difficulty': 'medium', 
        'question': 'In which city did American rap producer DJ Khaled originate from?',
        'correct_answer': 'Miami', 
        'incorrect_answers': [
            'New York', 
            'Detroit', 
            'Atlanta'
            ]
        }
]
"""