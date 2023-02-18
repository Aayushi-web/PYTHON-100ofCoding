import random
money=200
print("Answer few question and win $200 each")
question=["In which country is located World largest trade centre of diamond?","Chomolungma is located in which country?","Which is the nearest star to the Sun ?"
]

ques=random.choice(question)
print(ques)
answer=input("enter your answer: ")
print(answer)

if(answer=="belgium"and ques=="In which country is located World largest trade centre of diamond?"):
    print("keep it upp an u got $200")
  
elif (answer=="Apollo" and ques=="Which is the nearest star to the Sun ?") :
    print("keep it upp an u got $200")
elif (answer=="Nepal" and ques=="Chomolungma is located in which country?") :
    print("keep it upp an u got $200")
else:
   print("ohhh nooo u aree wrong")
