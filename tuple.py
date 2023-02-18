# tup=(4,0)
# print(type(tup),tup)
# print(tup[-1])
# if 4 in tup:
#     print("yesss")
#     #method  in tuple
countries=("spain","Italy","India","England","Germany")
temp=list(countries)
temp.append("Russia")
temp.pop(3)
temp[2]="Finland"
countries=tuple(temp)
print(countries)