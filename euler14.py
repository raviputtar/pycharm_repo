import time
maxlength=0

stime=time.time()

length_of={}
def find_length(x):
    chain=1
    while (x != 1):
        if x % 2 == 0:
            x = x // 2
        else:
            x = 3*x + 1
        if x in length_of:
            chain=chain+length_of[x]
            break
        else:
            chain=chain+1
    return chain

starting_no=0
for i in range(1,1000002):
    length=find_length(i)
    length_of[i]=length
    if length> maxlength:
        maxlength=length
        starting_no=i
print(starting_no,maxlength)

etime=time.time()
print("time_taken-->",etime-stime)
