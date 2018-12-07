mypalinlist=[]
mybinaryhash={}
def check_palin(x):
    mynumlist=list(map(int,str(x)))
    length=len(mynumlist)
    s=0
    res=1
    while (s<=length // 2):
        if mynumlist[s] == mynumlist[length-1-s]:
            res=1
        else:
            res=0
            break
        s=s+1
    return res


def check_palin_base2(t):
    mybinarynum=[]
    res=0
    x=t
    while x >0:
        num=x % 2
        mybinarynum.append(num)
        x=x // 2
    mybinarystring=''.join(str(e) for e in mybinarynum)
    if mybinarystring == mybinarystring[::-1]:
        res=1
    else:
        res=0
    if res:
        mybinaryhash[t]=mybinarystring
    return res

i=1
while i < 1000000:
   if check_palin(i):
       if check_palin_base2(i):
           mypalinlist.append(i)
   i=i+1





print(mypalinlist)
print(sum(mypalinlist))
print(mybinaryhash)




