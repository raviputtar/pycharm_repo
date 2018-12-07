import math
def check_prime(x):
    if x < 0:
        return False
    if x == 1:
        return False
    elif x == 2 :
        return True
    elif x % 2 == 0:
        return False
    else:
        root=math.sqrt(x)
        i=3
        res=True
        while(i<=root):
            if x % i == 0:
                res=False
                break
            i=i+2
        return res

maxcount=0
maxa=0
maxb=0

for a in range(-999,1000):
    for b in range(-1000,1001):
        dtest=a*a-4*b
        # if dtest <= 0:
            # print(dtest, a, b)
        if dtest >= 0 or dtest <=0:
            n=0
            count=0
            while True:
               value=n*n+a*n+b
               if check_prime(value):
                   count=count+1
               else:
                   break
               n=n+1
            if count>maxcount:
                maxcount=count
                maxa=a
                maxb=b


print(maxcount,maxa*maxb)


