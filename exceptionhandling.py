a=input(f"enter the number :")
print(f"multipliction of a table{a} is:")
try:
    for i in range(1, 11):
     print(f"{int(a)}X{i} = {int(a)*i}")
except IndexError:
    print ("sorry some erroe occured")    
print("some lines of code")
print("end of programm")    