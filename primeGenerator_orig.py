mydict = {}
def primes(y,x):
    for i in range(y,x+1):
        mydict[i] = 1

    for i in range(int (y/2),x+1):
        p = i
        if p in mydict and mydict[p] == 1:
            count = 2
            while p <= x+1:
                p = i * count
                # print("p=",p)
                if p in mydict:
                    mydict[p] = 0
                count = count + 1

t=int(input())
mytest=[]
mytestlist=[]
current={}
for i in range(0, t):
    mytest=[]
    mytest=input().split()
    mytestlist.append(mytest)

large=0
for i in mytestlist:
    if int(i[1])>large:
        large=int(i[1])

primes(large)

for i in mytestlist:
    check_from = int(i[0])
    check_till = int(i[1])
    for cp in current:
        if current[cp] == 1 and int(cp) >= check_from and int(cp) <= check_till:
            print(cp)
    print("\n")