#factorial (7)= 7*6*5*4*3*2*1
# #factorial (0)=1
# factorial= n*factorial(n-1)
def factorial (n):
    if(n==1 or n==0):
        return 1
    else:
         return  n*factorial(n-1)    

print(factorial(3))         

# f0=0
# f1=1
# f2=f1+f0
# f(n)=f(n-1)+f(n-2)
def fibonacci(n):
    if(n==1):
        return 1
    else:
        return (n*fibonacci(n-1))    
   

print(fibonacci(5))   