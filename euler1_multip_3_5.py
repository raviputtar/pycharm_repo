import sys
import time

time1=time.time()

def get_sum(n):
    myset=set()
    for i in range(1,n):
        test1=i*3
        test2=i*5
        if test1 < n:
            myset.add(test1)
            myset.add(test2)
        else:
            print(test1, n)
            break
    return (sum(myset))

def get_sum2(n):
    print(sum(set(list(range(0, n, 3)) + list(range(0, n, 5)))))



# t = int(input().strip())
#
# mytestlist = []
#
# for a0 in range(t):
#     n = int(input().strip())
#     mytestlist.append(n)
#
# for i in mytestlist:
#     print(get_sum(i))

get_sum2(1000000000)
time2=time.time()

print("time taken -->",time2-time1)