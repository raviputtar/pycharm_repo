import re
n=int(input())
myres="invalid"
for i in range(n):
    mystr=input()
    if len(set(mystr))<10 or len(set(mystr))>10:
        myres="invalid"
    if len(set(mystr))==10:
        upper=re.compile(r'[A-Z]')
        myupper=upper.findall(mystr)
        if len(myupper)>2 and len(myupper)<=7:
            digits=re.compile(r'\d')
            print(mystr)
            mydigits=digits.findall(mystr)
            if len(mydigits)>=3 and len(mydigits)<=8:
                myres="valid"
    print(myres)