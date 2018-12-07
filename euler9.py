import math
import time

start_time=time.time()

mydict={}
for i in range(1,998):
    isq=i**2
    mydict[isq]=i

count=0
res=1
for i in range(1,997):
    for j in range(2,998):
        isquare=i**2
        jsquare=j**2
        # mydict[isquare]=i
        # mydict[jsquare]=j
        count=count+1
        sumsquare=isquare+jsquare
        if sumsquare in mydict:
            print ("c2=",sumsquare,"a2,b2=",isquare,jsquare,"a,b=",i,j)
            if (mydict[sumsquare]+mydict[isquare]+mydict[jsquare]) == 1000:
                print(mydict[sumsquare]*mydict[isquare]*mydict[jsquare])
                print(count)
                res=0
                break
    if(res==0):
        break
print ("time taken-------->",time.time()-start_time)


start_time2=time.time()

for i in range(1,997):
    for j in range(2,998):
        isquare=i**2
        jsquare=j**2

print ("time taken-------->",time.time()-start_time2)