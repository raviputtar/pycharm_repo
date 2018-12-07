str="""73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450"""


# mylist=[]
# for line in str.split("\n"):
#     mylist.append(line)
# print(mylist)
#
# for i in range(0,len(mylist[0])):
#

string_length=len(str)
print(string_length)
str=str.strip('\n')
str=str.replace('\n',"")

string_length=len(str)
print(string_length)

max_pro=1
for i in range(0,len(str)-12):
    local_pro=1
    for j in range(i,i+13):
        local_pro=local_pro*int(str[j])
    if local_pro > max_pro:
        max_pro=local_pro
print(max_pro)
# max_pro=1
# for line in str.split("\n"):
#     # print("line=",line)
#     # # print(len(line))
#     # # # print("line 0 =",line[0])
#     for i in range(0,len(line)-12):
#         #print("i=",i, )
#         local_pro=1
#         for j in range(i,i+13):
#             # if (int(line[j]) == 0):
#             #     local_pro=0
#             #     break
#             local_pro=local_pro*int(line[j])
#             # print("str j is:",str[j])
#             # print("local pro now is:",local_pro)
#             # print("j=",j,"line[j]=",int(line[j]))
#
#      #    print("local=",local_pro)
#         if local_pro > max_pro:
#             max_pro=local_pro
#         #print("max=",max_pro)

# print("max=",max_pro)


# max_pro=0
# i=0
# while i <= len(str):
#     local_pro=1
#     print("length is",len(str))
#     current_length=i+12
#     if current_length == len(str):
#         break
#     if str[i+12] == "\n":
#         i=i+13
#     for j in range(i,i+13):
#         if j == i+13:
#             print ("j=",j)
#         local_pro=local_pro*int(str[j])
#     if local_pro > max_pro:
#         max_pro=local_pro
#     i=i+1
#
# print(max_pro)

#     local_sum=0
#     if str[i+13] != "\n":
#         for j in range(i,i+13):
#                 local_sum=local_sum+int(str[j])
#         if local_sum > max_Sum:
#             max_Sum=local_sum
# print(max_Sum)

# for

