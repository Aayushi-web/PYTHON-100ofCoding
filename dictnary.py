# dic ={
#     1:"mishra",
#     5:"fock"
# }
# print(dic.get(1))
# print(dic.keys())
# print(dic.values())


# for i in dic.keys():
#     print(f" the  value if  {i}  and their corresponding values are {dic[i]} ")
# print(dic.items())
# for key,value in dic.items():
#     print(f"the value of {key} and its corresponding value is {dic[key]}")
emp={
    122:45,
    123:89,
    124:670
}
emp2={
    222:67,
    566:90
}
emp.update(emp2)
print(emp)
# emp.clear()
# print(emp)
emp.popitem()
print(emp)
print(type(emp))