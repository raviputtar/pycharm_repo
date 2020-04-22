# #this is just a test file to see if it gets uploaded
# # a=input("enter a string:")
# # print("reverse of string is:",end="")
# # print(a[::-1])
#
# # myfunc=lambda x,y:x+y*y
# #
# # print(myfunc(0,2))
#
# mystr="123456"
# print(id(mystr))
# mystr="123"
# print(list(map(int,mystr)))
#
# # myeven=(list(filter(lambda x:x%2==0,[2,3,4,5,6,7,8,9]])))
# #
# # print(myeven)
#
# print(id(mystr))
#
# a = "Foo"
# # a now points to "Foo"
# b = a
# # b points to the same "Foo" that a points to
# a = a + a
# # a points to the new string "FooFoo", but b still points to the old "Foo"
#
# print ("a=",a)
# print (b)
# # Outputs:
#
# # FooFoo


# class myTestClass:
#     name="ravinder"
#     rollno=23
#     def __init__(self,name,school):
#         self.name=name
#         self.school=school
#     def dispaly(self):
#         print(self.name)
#         print(self.school)
#         print(self.rollno)
#
# myobj=myTestClass("sachin","gtbit")
#
# myobj.dispaly()
#
#
# class mySecClass(myTestClass):
#     batting=""
#     bowling=""
#     def __init__(self,batting,bowling):
#         self.batting=batting
#         self.bowling=bowling
#     def dispaly(self):
#         print(self.name)
#         print(self.bowling)
#         print(self.batting)

mylist=[1,2,3]
t1=(1,2,5)
print(id(t1))
t2=(3,7,10)
t1=t1+t2
print(id(t1))
print(t1)





mydict={}
mystr="1234562343333@@Asdasdas@VSF%%^"
for i in mystr:
    if i in mydict:
        mydict[i]=mydict[i]+1
    else:
        mydict[i]=1

print(mydict)



mylist1=[1,2,3]
mylist2=[1,3,5]
print(mylist1+mylist2)
