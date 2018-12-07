import re

text="""my name is ravinder singh saini i have emp code 0-23 and 0*23 " \
     "phone no is 7838236538\r" \
     "like to play football" \
      name is sachin emp code 0-24 """

pattern= re.compile(r'name\sis\s')

matches=pattern.finditer(text)

for m in matches:
    print(m)


