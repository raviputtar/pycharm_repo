dict={}

for i in range(2,1001):
    j=1
    count=0
    mydict = {}
    while True:
        while j <= i:
            j=j*10
        print(i, j)
        if j % i == 0:
            break
        else:
            count=count+1
            rem = j % i
            print("rem is:",rem)
            if rem in mydict:
                break
            else:
                mydict[rem] =1
                j=rem
    dict[i]=count

max=0
maxnum=0
for i in dict:
    if dict[i]> max:
        max=dict[i]
        maxnum=i

print(maxnum,max)







