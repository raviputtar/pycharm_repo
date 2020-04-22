for i in range(1,1000000):
    one=str(i)
    two=str(2*i)
    three=str(3*i)
    four=str(4*i)
    five=str(5*i)
    six=str(6*i)

    if set(one)==set(two):
        if set(two)==set(three):
            if set(three)==set(four):
                if set(four)==set(five):
                    if set(five)==set(six):
                        print("number found",i,one,two,three,four,five,six)
                        exit()
    else:
        print("not found")
