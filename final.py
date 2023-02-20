def func1():
    try:
       l=[1,5,64,1]
       i= int(input("enter your num"))
       print(l[i])
    except:
       print("some error occur")
       return 0


    finally:
     print("I am always executed ") 

x= func1()
print(x)
