import time
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


all_primes={}
all_primes=primes(10000)


mylist=[]
for key in all_primes:
    if all_primes[key]==1:
        p=str(key)
        if len(p)==4:
            mylist.append(p)

print(mylist)
for s in mylist:
    count=0
    matched=[]
    for j in mylist:
       # print("s now is,",s,"j is",j)
        if int(s) == int(j):
            pass
        else:
            slist=list(s)
            jlist=list(j)
            if set(slist) == set(jlist):
                if count == 0:
                    matched.append(int(j))
                    count+=1
                    diff=int(j)-int(s)
                if count ==1 :
                    if int(j)-matched[0] == diff:
                        matched.append(int(j))
                        print("nofound",s,matched)
                        count+=1




        if count==2:
            matched.sort()
            print("no_found", s, matched)
            if matched[1] - matched[0]== matched[0] - int(s):
                print("no_found", s, matched)
            break




endtime=time.time()

print("time_taken-->",endtime-starttime)
