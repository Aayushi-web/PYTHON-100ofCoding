# s={2,8,655,655,89,89}
# print(s)
# info=("19",19,True,5.6)
# print(info)
# s1=set()
# print(type(s1))
# for v in info:
#     print(v)

s1={1,5,5,6,3,10}
s2={7,8,8,6}
print(s1.union(s2))
print(s1.intersection(s2))
s3=s1.update(s2)
print(s1.symmetric_difference(s2))
print(s2.difference(s1))
print(s1.isdisjoint(s2))
print(s1.issuperset(s2))
print(s1.add(45))
print(
s1.pop())
print(s1.remove(5))
