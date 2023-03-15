import random
op="swg"
computer=random.choice(op)
user=(input(" w for water , s for snake, g for gun "))
print("computer ",computer)
print("user",user)
if(computer==user):
    print("ots a draw")
elif(computer=="s" and user=="w"):
    print("computer won")
elif(computer=="w" and user=="g"):
    print("computer won")






