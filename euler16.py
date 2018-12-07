import time
st=time.time()
mynum=2**1000

mylist=map(int,list(str(mynum)))

result=sum(mylist)
print(result)

et=time.time()
print("time taken-->",et-st)