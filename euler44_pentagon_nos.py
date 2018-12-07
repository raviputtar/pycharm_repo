penta_dict=dict()
penta_dict={1:1}
max_diff=0
breakout=0
n=2
while n<11:
    pentagon_no=n*(3*n-1)//2
    print("n now is-->",n,"pent no-->",pentagon_no)
    penta_dict[pentagon_no]=n
    penta_list=list(penta_dict)
    nextpenta=(n+1)*(3*(n+1)-1)//2
    for i in range(0,len(penta_list)):
        if breakout==1:
            break
        else:
            for j in range(i+1,len(penta_list)):
                penta_sum=penta_list[j]+penta_list[i]
                penta_diff=penta_list[j]-penta_list[i]
                if penta_sum in penta_dict and penta_diff in penta_dict:
                    if penta_diff > max_diff:
                        max_diff=penta_diff
                        print(max_diff)
                elif penta_sum> penta_list[-1] and penta_diff in penta_dict:
                    t=n+1
                    while True:
                        next=t*(3*t-1)//2
                        if next == penta_sum:
                            if penta_diff>max_diff:
                                max_diff=penta_diff
                                break
                        elif next>penta_sum:
                            break
                        else:
                            t=t+1
                else:
                    pass

                if max_diff> (nextpenta-penta_list[-1]):
                    print("endpoint reached")
                    breakout=1
    n=n+1

print("max_diff-->",max_diff,penta_sum,n)





