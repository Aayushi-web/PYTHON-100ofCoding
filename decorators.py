

def greet(fx):
    def mfx():
        print("good morning")
        fx()
        print("thanks for using this functions")
        return mfx
    

 
def hello():
    print("hello world")

  

def add(a,b):
    print(a+b)


greet(hello)()