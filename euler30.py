maxval=0

digit_power_sum=9**5+9**5
smallest_digit_num=10
my_power_digits=[]
while digit_power_sum > smallest_digit_num:
    num=smallest_digit_num
    while num < smallest_digit_num*10:
        strnum=str(num)
        numlist=list(strnum)
        su=0
        for j in numlist:
            j=int(j)
            su=su+j**5
        if num == su:
            my_power_digits.append(num)
        num=num+1
    digit_power_sum=digit_power_sum+9**5
    smallest_digit_num=smallest_digit_num*10

print(my_power_digits)
print(sum(my_power_digits))

