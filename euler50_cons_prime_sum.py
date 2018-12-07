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
    mydictnew={}
    for i in range(2,x+1):
        if mydict[i]==1:
            mydictnew[i]=1

    return mydictnew

prime_dict={}
prime_dict=primes(1000000)
prime_list=list(prime_dict)


sum=0
maxchain_till_now=0
starting_point=0
mymax_num=0
for i in range(0,len(prime_list)):
    mysum=prime_list[i]
    count=1
    maxchain=0
    max_prime=0
    for j in range(i+1,len(prime_list)):
        mysum=mysum+prime_list[j]
        count=count+1
        if mysum > prime_list[len(prime_list)-1]:
            break
        elif mysum in prime_dict:
            maxchain=count
            max_prime=mysum
        else:
            pass

    if maxchain > maxchain_till_now:
        maxchain_till_now=maxchain
        starting_point=prime_list[i]
        mymax_num=max_prime

etime=time.time()
print("maxchain:",maxchain_till_now,"starting point:",starting_point,"ma max num:",mymax_num,"time:",etime-stime)



