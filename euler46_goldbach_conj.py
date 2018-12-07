import time
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
    mynewdict={}
    for i in mydict:
        if mydict[i]==1:
            mynewdict[i]=1

    return mynewdict

myprimes=primes(1000000)
print(myprimes)

def check_conjecture(n):
    for m in myprimes:
        res=True
        if m < n:
            j=1
            while True:
                value=m+2*(j**2)
                if value == n:
                    res=False
                    print("prime=",m,"square==",j,"num=",n)
                    break
                elif value<n:
                    pass
                else:
                    break
                j=j+1
        else:
            break
        if res==False:
            break

    return res

i=3
while True:
    if i not in myprimes:
        # print("checking i-->",i)
        if check_conjecture(i):
            print("number is:",i)
            break
        else:
            print("i follows conjecture")
    i+=2

etime=time.time()
print("time taken-->",etime-stime)