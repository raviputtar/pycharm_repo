
t=int(input())
mytest=[]
mytestlist=[]
for i in range(0, t):
    mytest=[]
    mytest=input().split()
    mytestlist.append(mytest)

large=0
for i in mytestlist:
    if int(i[1])>large:
        large=int(i[1])





x=large // 2
print(x)
nonprimelist=[]
for i in range(1,x+1):
    nonprimelist.append(i)

for i in range (1,x+1):
    for j in range(1,x+1):
        test=i+j+2*i*j
        if test in nonprimelist:
            nonprimelist.remove(test)

def primeGen():
    yield 2
    for i in nonprimelist:
        yield 2*i+1

print(nonprimelist)
for i in mytestlist:
    check_from = int(i[0])
    check_till = int(i[1])
    for p in primeGen():
        if p >= check_from and p <=check_till:
            print(p)
