import re
n=int(input())
colorlist=[]
for i in range(n):
    line=input()
    pattern=re.compile(r'(?<!\A)#[0-9a-f]{3,6}',re.I)
    mycolours=pattern.findall(line)
    print(mycolours)
    if mycolours:
        for m in mycolours:
            colorlist.append(m)
for c in colorlist:
    print(c)