class Employee:
    company_name="Google"
    no_ofEmpl=0
    def __init__(self,name):
        self.name=name
        self.raised_amount=0.5
        Employee.no_ofEmpl+=1
    def showDetails(self):
        print(f"the name of the Employee is{self.name}in {self.no_ofEmpl} and their raised amount is {self.raised_amount} also he worked in  {self.company_name} ")    
empl=Employee("aayushi")
emp2=Employee("ekta")
empl.showDetails()
emp2.showDetails()
# Employee.showDetails(empl)