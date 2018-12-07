import math
import time
starttime=time.time()
def primes(x):
    mydict={}
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
    for i in list(mydict):
        if mydict[i]==0:
            del mydict[i]
    return mydict

prime_factors={}
prime_factors=primes(100000)




def getPrimeFactors(t):
    factor=1
    root=math.sqrt(t)
    for i in prime_factors:
        if i > root:
            break
        else:
            if t % i == 0:
                pow=1
                tester=i
                while tester <= t:
                    tester = tester*i
                    if t % tester == 0:
                        pow = pow+1
                    else:
                        break
                factor=factor*(pow+1)
                # print("factor now=",factor)
    return factor

n=2
while True:
    triangularno=n*(n+1) // 2
    fact=getPrimeFactors(triangularno)
    print(triangularno,fact)
    if fact > 500:
        print ("found no --> It is",triangularno)
        break
    n=n+1


endtime=time.time()

print("time_taken-->",endtime-starttime)










