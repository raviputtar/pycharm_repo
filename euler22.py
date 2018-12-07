import string
a=open(r'C:\Users\rsingh\PycharmProjects\euler\p022_names.txt','r')
mystr=a.read()
mylist=mystr.split(",")
mylist.sort()

chars={}

i=1
for char in string.ascii_uppercase:
    chars[char]=i
    i=i+1

sum=0
count=1
for i in mylist:
    temp=0
    for j in list(i[1:len(i)-1]):
        temp=temp+chars[j]
    sum=sum+temp*count
    count=count+1

print(sum,count)