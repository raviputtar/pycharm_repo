
n = 21
m = 21

def lattice_paths(n,m):
    a = [0] * n
    for i in range(n):
        a[i] = [0] * m
    for i in range(0,n):
        for j in range(0,m):
            if i == 0 or j == 0:
                a[i][j]=1
            else:
                a[i][j]=a[i-1][j]+a[i][j-1]
    print(a)



t=0
a=[]
temp=0
t = int(input())
for i in range(0,t):
    x,y=input().split()
    a[i].append(int(x))


for i in a:
    for j in a[i]:
        print(lattice_paths(j[0],j[1]))