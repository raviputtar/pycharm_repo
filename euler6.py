sum_n=lambda n: (n**2 * (n+1)**2) // 4
sum_square_n=lambda n: (n*(n+1)*(2*n+1)) // 6

def get_diff(x):
    print (sum_square_n(x)-sum_n(x))



t=0
a=[]
temp=0
t = int(input())
for i in range(0,t):
    temp=int(input())
    a.append(temp)

for i in a:
    get_diff(i)
