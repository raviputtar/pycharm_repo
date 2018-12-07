import math
import time
start_time=time.time()
count=1
prime_list=[2]
# def chk_prime(x):
#     root=math.sqrt(x)
#     res=True
#     p=3
#     while p <= root:
#         if x % p == 0:
#             res=False
#             break
#         p=p+1
#     return res

# def chk_new():
#     for i in range (3,200000,2):
#         root=math.sqrt(i)
#         for j in prime_list:
#             res=True
#             if j <= root:
#                 if i % j == 0 :
#                     res=False
#                     break
#         if res :
#             prime_list.append(i)

sum=0
chk_new()
for i in range(2,2000000):
    mylist.append(i)

for i in mylist:
    count=1
    while i <= mylist[-1]:
        i=i*count
        for j in mylist:
            if j % i == 0:
                mylist.remove(j)
        count=count+1


for i in prime_list:
    sum=sum+i
    count+=1

print(sum)
print(count)
endtime=time.time()
print("time taken=",endtime-start_time)