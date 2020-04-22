
## 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
coins=[1,2,5,10,20,50,100,200]
N=5
ways=[]
ways.append(1)
for i in range(1,N+1):
    ways.append(0)

def getways(coin,ways):
    for j in range(N+1):
        if coin > j :
            ways[j]=ways[j]
        elif coin <= j:
            ways[j]=ways[j-coin]+ways[j]


for i in coins:
    getways(i,ways)
    for i in ways:
        print(i,end=" ")
    print(",")


print(ways[N])

