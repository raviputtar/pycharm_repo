import re
n=int(input())
mystring=""
for i in range(n):
    line=input().strip()
    mystring=mystring+" "+line

print(mystring)
  #  pattern = re.compile(r'(<!--.*-->)', re.I)
pattern = re.compile(r'<([a-z]+)(\s([a-z]+)="(.*?)")*/?>+', re.I)
matches=pattern.findall(mystring)
# if matches:
#     print(matches)
    # print("grp1=",matches.group(1))
    # print("grp2=",matches.group(2))
    # print("grp3=",matches.group(3))
    # print("grp4=", matches.group(4))
for i in matches:
    print(i)
