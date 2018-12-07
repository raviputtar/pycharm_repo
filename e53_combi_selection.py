fact_dict={}

def fact(f):
    if f in fact_dict:
        return fact_dict[f]
    elif f ==1 or f ==0:
        return 1
    else:
        return f*fact(f-1)

for i in range(1,101):
    fact_dict[i]=fact(i)

print(fact_dict)

greater=0
for n in range(1,101):
     for r in range(1,n):
         nume= fact(n)
         deno=fact(r)*fact(n-r)
         ncr_value=nume // deno
         if n == 23 and r ==10:
             print("ncrvalue for",n,r,"is",ncr_value)
         if ncr_value > 1000000:
             greater=greater+1

print(greater)


