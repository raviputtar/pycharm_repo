import os
mydir=os.getcwd()
print("c/n dir=",mydir)
for i in os.walk(mydir):
    print(i)