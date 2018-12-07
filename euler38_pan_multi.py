mypanlist=[]
def createPan(n):
    mylist=[]
    i=1
    while True:
        mylist.append(n*i)
        mystrlist=''.join(str(e) for e in mylist)
        length=len(mystrlist)
        if length>9:
            break
        elif length ==9:
            if check_pan(mystrlist):
                mypanlist.append(mystrlist)
        else:
            pass
        i=i+1

def check_pan(mystring):
    print("mystring=",mystring)
    myotherlist=[]
    # myotherlist=list(mystring)
    myotherlist=list(map(int,mystring))
    print(myotherlist)
    mydict={}
    for i in myotherlist:
        mydict[i]=1

    print(mydict)
    res=True
    for i in range(1,10):
        if i not in mydict:
            print(i,"not in")
            res=False
            break
        else:
            pass
    print("res now is:",res)
    return res

for i in range(1,10000):
    createPan(i)

print(max(mypanlist))



