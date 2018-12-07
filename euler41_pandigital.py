import time
import math
starttime=time.time()
mydict={}

max_prime=0
length=0
mynum=[]
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
    mydictnew={}
    for i in range(2,x+1):
        if mydict[i]==1:
            mydictnew[i]=1

    return mydictnew

def check_prime(x):
    if x == 1:
        return False
    elif x == 2:
        return True
    elif x % 2 == 0:
        return False
    else:
        root = math.sqrt(x)
        i = 3
        res = True
        while (i <= root):
            if x % i == 0:
                res = False
                break
            i = i + 2
        return res

all_primes={}
all_primes=primes(987654322)

for i in all_primes:
    mynum=list(map(int,str(i)))
    res=True
    for j in range(1,len(mynum)+1):
        if j in mynum:
            res=True
        else:
            res=False
            break
    if res:
        if i > max_prime:
            max_prime=i

print(time.time())
def check_pan(i):
    mynum = list(map(int, str(i)))
    res = True
    for j in range(1, len(mynum) + 1):
        if j in mynum:
            res = True
        else:
            res = False
            break
    return res


for i in range(10000001, 987654322,2):
    if check_prime(i):
        print("checking-->",i)
        if check_pan(i):
            if i > max_prime:
                max_prime = i


etime=time.time()
print("time taken-->",etime-starttime)

print(max_prime)
