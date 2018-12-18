import os
mydir=os.getcwd()
print("c/n dir=",mydir)
for dirname,dirpath,filename in os.walk(mydir):
    print("dirname:",dirname)
    print("dirpath:",dirpath)
    print("file:",filename)
    if filename.find("euler67.py"):
        print("file found,it is:",filename)
        break


