#dictionary = {[School: Rocklin High], [Address: Victory Ln], [Founded: 1992]}

# dictionary = {
#     "response_code": 0,
#     "results": [
#         {
#             "category": "Animals",
#             "type": "boolean",
#             "difficulty": "easy",
#             "question": "A slug&rsquo;s blood is green.",
#             "correct_answer": "True",
#             "incorrect_answers": [
#                 "False"
#             ]
#         }]}

# dictionary = [
#     {
#         "results.category": "General Knowledge",
#         "results.type": "boolean",
#         "results.difficulty": "medium",
#         "results.question": "Coca-Cola&#039;s original colour was green.",
#         "results.correct_answer": "FALSE",
#         "results.incorrect_answers.0": "TRUE",
#         "results.incorrect_answers.1": "",
#     }]

# question_data = dictionary["results"]
# print(question_data)
dictionary = {
    "School":["Rocklin High", "Whitney High"], 
    "Founded":1900, 
    "Grades":[{"Student":"Amari","Subject":"Math","Grade":99.3}, 
              {"Student":"Bob","Subject":"Physics","Grade":23.75}]
              }

print(dictionary["School"])
print(dictionary["Founded"])
for value in dictionary.items():
   print(value[0])

for value in dictionary.items():
    if value[0] == "Grades":
        for x in value[1]:
            for newvalue in x.items():
                print(newvalue[0], newvalue[1])

for g in dictionary["Grades"]:
    for k,v in g.items():
        print(k, v)

#possible to do in a single line - look into later