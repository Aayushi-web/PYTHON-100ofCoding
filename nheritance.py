class  Employee:
    def __init__(self, name,id):
       self.name=name
       self.id=id
    def show_details(self):
        print(f"the name of employee:{self.id } is {self.name}")   
class Programmer(Employee):
    
    def showLanguage(self):
        print("the default lamguage is python")        
e= Programmer("aayushi",123)
e.show_details()

e1= Employee("anishka",153)
e1.show_details()  
