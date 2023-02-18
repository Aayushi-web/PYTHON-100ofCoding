import random
print("Answer few question and win $200 each")
question=["In which country is located World largest trade centre of diamond?","Chomolungma is located in which country?","Which is the nearest star to the Sun ?"
]
ques=random.choice(question)
print(ques)
answer=input("enter your answer: ")
if (question=="In which country is located World largest trade centre of diamond"and answer=="belgium"):
    print("keep it upp an u got $200")