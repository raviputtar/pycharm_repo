# def fact(n):
#     if n==1 or n==0:
#         return 1
#     else:
#         print ("n=",n)
#         return n*fact(n-1)
#
# print(fact(6))
i=1
while i <=5 :
    for t in range(i):
        print("* ",end="")
    print("\n")
    i+=1

print("\x48\x49!")



try:
    with open(r"C:\Users\rsingh\PycharmProjects\euler\e53_combi_selection.py",'r') as f:
        while f.readline():
            data=f.readline()
            print(data)
except IOError:
    print("file not found")
# print(mylist[-7:-3])

for i in range(10):
    print(i,end=" ")





