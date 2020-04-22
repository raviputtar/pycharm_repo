import time
key=0
mydict={}
myprod={}
stime=time.time()
for i in range(1,350):
    for j in range(i,700):
        for k in range(j,1000):
            # print("ijk now is",i,j,k)
            if i*i + j*j < k*k:
                break
            if i*i + j*j == k*k:
                # print("ijk for key is",i,j,k)
                key=i+j+k
                if key <= 1000:
                    if key not in mydict:
                        mydict[key]=1
                    else:
                        mydict[key]=mydict[key]+1


max=0
max_sol=0
for t in mydict:
    if mydict[t] > max:
        max=mydict[t]
        max_sol=t

print("maxp=",mydict[max_sol],"maxsolutions=",max_sol)
etime=time.time()
print("timetaken-->",etime-stime)



