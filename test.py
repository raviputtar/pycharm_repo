# import sys
list1=[]
for i in range(1,10):
    list1.append(i)
print(list1)
print(list1[0:9])
#
# # Python code to demonstrate range() vs xrange()
# # on  basis of return type
#
# # initializing a with range()
# a = range(1, 10000)
#
# # initializing a with xrange()
# x = xrange(1, 10000)
#
# # testing the type of a
# print("The return type of range() is : ")
# print(type(a))
#
# # testing the type of x
# print("The return type of xrange() is : ")
# print(type(x))

import functools

large=functools.reduce(lambda  a,b:a if a> b else b,list1)
print(large)
add=filter(lambda x:  x % 2 == 0,list1)

print(list(add))