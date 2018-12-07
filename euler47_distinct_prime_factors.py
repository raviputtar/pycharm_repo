import time
import math
stime=time.time()
mydict={}
def primes(x):
    for i in range(2,x+1):
        mydict[i] = 1

    for i in range(2,x+1):
        p = i
        if p in mydict and mydict[p] == 1:
            count = 2
            while p <= x+1:
                p = i * count
                # print("p=",p)
                if p in mydict:
                    mydict[p] = 0
                count = count + 1
    return mydict


mydict2=dict()
mydict2=primes(1000000)
root=0
def getfactors(i):
    factors=[]
    root=int(math.sqrt(i))
    for j in range(2,root+1):
        if i % j == 0:
            if i // j != j:
                factors.append(i//j)
                factors.append(j)
            else:
                factors.append(j)
    prime_counter=0
    for f in factors:
        if mydict2[f] ==1:
            prime_counter=prime_counter+1
    return prime_counter


n=2
while True:
    factors=getfactors(n)
    # print("factors for",n," are -->",factors)
    if factors == 4 :
        if getfactors(n+1) == 4:
            if getfactors(n+2) == 4:
                if getfactors(n+3) == 4:
                    print("number found-->",n )
                    break
    n=n+1

etime=time.time()
print("time taken-->",etime-stime)


