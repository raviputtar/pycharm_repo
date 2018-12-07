import math

def check_prime(x):
    root=math.sqrt(x)
    i=2
    res=True
    while(i<=root):
        if x % i == 0:
            res=False
            break
        i=i+1
    return res

prime_20=[]
for i in range(2,20):
    if check_prime(i):
        prime_20.append(i)

prime_power={}
for i in prime_20:
    x=i
    pow=0
    while (x<=20):
        pow=pow+1
        x=x*i
    prime_power[i]=pow

lcm=1
for key,value in prime_power.items():
    print('key=',key,'pow=',value)
    lcm=lcm*(key**value)
    print (lcm)










