import time
from typing import List

starttime=time.time()
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

count=0
all_primes=primes(1000000)
# print(all_primes)
mynumlist_right=[]
mynumlist_left=[]
mystrnum_right=0
mystrnum_left=0
length=0
my_truncatable_primes=[]
def get_primes():
    count=0
    for i in all_primes:
        result=1
        if all_primes[i]==1:
            mynumlist_right=list(map(int,str(i)))
            mynumlist_left=mynumlist_right.copy()
            length=len(mynumlist_right)
            print(length)
            loop_run=length-1
            while loop_run != 0 and result == 1:
                popped=mynumlist.pop(length-1)
                mynumlist_left.pop(0)
                mystrnum_right=''.join(str(e) for e in mynumlist_right)
                print(mystrnum_right)
                mystrnum_left =''.join(str(e) for e in mynumlist_left)
                print(mystrnum_left)
                mystrnum=int(mystrnum)
                if mystrnum_right in all_primes and all_primes[mystrnum_right] == 1 and mystrnum_left in all_primes and all_primes[mystrnum_left] == 1:
                    result==1
                    loop_run=loop_run-1
                else:
                    result=0
            if result==1:
                my_truncatable_primes.append(i)
    return count

mycount=get_primes()
print(mycount)
print(my_truncatable_primes)






endtime=time.time()

print("time_taken-->",endtime-starttime)



