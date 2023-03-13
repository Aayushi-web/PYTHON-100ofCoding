# import calendar
# print(calendar.calendar(2023))
# 
class MyClass:
    def __init__(self,value):
        self._value=value
    def show(self):
        print(f"values is {self._value}")    
    @property
    def value(self):
        return self._value    
obj=MyClass(10)    
obj.show()