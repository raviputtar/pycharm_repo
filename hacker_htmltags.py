import re
n=int(input())
mylist=[]
for i in range(n):
    line=input()
    pattern=re.compile(r'<(?![/!])([a-z]+)>',re.I)
    matches=pattern.findall(line)
    for i in matches:
        mylist.append(i)

for i in mylist:
    print(i)