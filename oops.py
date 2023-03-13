class Person:
    name="Aayushi"
    occupation="frontend Developer"
    networth="11"
    def info(self):
        print(f"{self.name} is a {self.occupation}")


a=Person()
b=Person()
a.name="anishka" 
# b.name="aryan"   
a.info()
b.info()