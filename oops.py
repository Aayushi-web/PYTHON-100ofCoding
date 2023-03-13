# class Person:
#     name="Aayushi"
#     occupation="frontend Developer"
#     networth="11"
#     def info(self):
#         print(f"{self.name} is a {self.occupation}")


# a=Person()
# b=Person()
# a.name="anishka" 
# # b.name="aryan"   
# a.info()
# b.info()
class Person():
    def __init__(self,name,occu):
        self.name=name
        self.occu=occu
    def info(self):
        print(f"My name is {self.name} and I am working as {self.occu}")
a=Person("aayushi","Developer")


a.info()    