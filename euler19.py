year=1900
month=[1,2,3,4,5,6,7,8,9,10,11,12]
days={}
days[1]=31
days[2]=28
days[3]=31
days[4]=30
days[5]=31
days[6]=30
days[7]=31
days[8]=31
days[9]=30
days[10]=31
days[11]=30
days[12]=31

count=0
rem=0
temp=0
month_days=0
while year <= 2000:
    print(year,count,rem)
    for i in month:
        if i == 2:
            if year % 4 == 0:
                if year % 100 == 0:
                    if year % 400 == 0:
                        temp=29
                else:
                    temp=29
        temp=days[i]
        month_days=temp+rem
        if month_days % 7 == 0:
            if year > 1900:
                count=count+1
                rem=0
        else:
            rem = month_days % 7
    year=year+1


print(count)






