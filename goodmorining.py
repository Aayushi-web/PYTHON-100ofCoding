import time
second= time.time()

locals= time.ctime(second)
print("local time",locals)
print("printed")
time.sleep(5)
print(" printed after 5 second")
result=time.localtime(second)
print(result.tm_hour)