import math
def check_prime(x):
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

def get_nth_prime(n):
    prime_count=0
    i=2
    while(prime_count<n):
        if check_prime(i):
            prime_count=prime_count+1
        if prime_count == n:
            print(i)
        if i == 2:
            i = i+1
        else:
            i=i+2


t=0
a=[]
temp=0
t = int(input())
for i in range(0,t):
    temp=int(input())
    a.append(temp)

for i in a:
    get_nth_prime(i)
