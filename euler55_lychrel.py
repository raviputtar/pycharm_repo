def check_palindrome(x):
    rev=x[::-1]
    if x==rev:
        return True
    else:
        return False


lychrel_count=0



def check_lychrel(num):
    count=0
    lychrel=True
    while (count!=50):
        rev=str(num)[::-1]
        #print("num=",num,"rev=",rev)
        palin=int(rev)+int(num)
        if check_palindrome(str(palin)) and len(str(palin))>1:
            print("palin_found=",palin)
            lychrel=False
            break
        else:
            count=count+1
            num=palin
    return lychrel

for i in range(1,10001):
    if check_lychrel(i):
        lychrel_count=lychrel_count+1



print(lychrel_count)
