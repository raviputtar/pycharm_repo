import sys



import math
def check_prime(x):
    root = math.sqrt(x)
    i = 2
    res = True
    while (i <= root):
        if x % i == 0:
            res = False
            break
        i = i + 1
    return res


def check_lcm(N):
    prime_20 = []
    for i in range(2, N+1):
        if check_prime(i):
            prime_20.append(i)
    prime_power = {}
    for i in prime_20:
            x = i
            pow = 0
            while (x <= N):
                pow = pow + 1
                x = x * i
            prime_power[i] = pow
    lcm = 1
    for key, value in prime_power.items():
        lcm = lcm * (key ** value)
    print(lcm)


t=0
a=[]
temp=0
t = int(input())
for i in range(0,t):
    temp=int(input())
    a.append(temp)

for i in a:
    check_lcm(i)

	
	
	#this has been edited
	