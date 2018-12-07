
a=open(r'C:\Users\rsingh\PycharmProjects\euler\p067_triangle.txt','r')
mystr=a.read()
mylist=mystr.split('\n')
temp=[]
# print(mylist)
final=[]
for i in mylist:
    if i is "":
        break
    else:
        temp=i.split(" ")
        temp=list(map(int,temp))
        final.append(temp)

for i in range(1,len(final)):
    for j in range(0,len(final[i])):
        if j == 0:
            final[i][j] = final[i][j] + final[i-1][j]
        elif j == len(final[i])-1:
            final[i][j]=final[i][j]+final[i-1][j-1]
        else:
            final[i][j]=final[i][j]+max(final[i-1][j],final[i-1][j-1])

m=0
for i in final:
    print(i)
for i in range(0,len(final)):
    for j in range(0,len(final[i])):
        if final[i][j]> m:
            m=final[i][j]

print(m)