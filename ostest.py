import os

print(os.getcwd())
os.chdir(r'C:\Users\rsingh\PycharmProjects')
print(os.getcwd())
#
for dirpath,dirnames,filenames in os.walk(os.getcwd()):
    print("c/n dir:",dirpath)
    print("Directories/:",dirnames)
    print("filenames:",filenames)


os.listdir()